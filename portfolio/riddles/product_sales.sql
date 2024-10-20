WITH MonthlySales AS (
    SELECT 
        productId,
        DATEPART(YEAR, saleDate) AS sale_year,
        DATEPART(MONTH, saleDate) AS sale_month,
        SUM(saleAmount) AS total_monthly_sales
    FROM 
        sales
    GROUP BY 
        productId, DATEPART(YEAR, saleDate),  DATEPART(MONTH, saleDate)
),
ConsecutiveSales AS (
    SELECT 
        productId,
        COUNT(DISTINCT CONCAT(sale_year, sale_month)) AS total_months,
        ROW_NUMBER() OVER (PARTITION BY productId ORDER BY sale_year, sale_month) AS month_rank
    FROM 
        MonthlySales
    GROUP BY  productId, sale_year, sale_month
    HAVING COUNT(*) >= 1
),
EligibleProducts AS (
    SELECT 
        ms.productId,
        SUM(ms.total_monthly_sales) AS totalSales,
        LAG(SUM(ms.total_monthly_sales)) OVER (PARTITION BY ms.productId ORDER BY ms.sale_year, ms.sale_month) AS previousMonthSales
    FROM 
        MonthlySales ms
    WHERE 
        (ms.sale_year = YEAR(GETDATE()) AND ms.sale_month = MONTH(GETDATE()))  -- Current month check
        OR (ms.sale_year = YEAR(GETDATE()) AND ms.sale_month = MONTH(GETDATE()) - 1)  -- Previous month check
    GROUP BY 
        ms.productId
)
SELECT 
    ep.productId,
    ep.totalSales,
    RANK() OVER (ORDER BY ep.totalSales DESC) AS salesRank,
    COALESCE(ep.previousMonthSales, 0) AS previousMonthSales
FROM 
    EligibleProducts ep
WHERE 
    EXISTS (SELECT 1 FROM ConsecutiveSales cs WHERE cs.productId = ep.productId AND cs.total_months >= 3)
GROUP BY 
    ep.productId, ep.totalSales, ep.previousMonthSales
ORDER BY 
    salesRank DESC;
