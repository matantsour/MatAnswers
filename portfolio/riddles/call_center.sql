SELECT worker_id
FROM (
    SELECT worker_id, SUM(call_duration) AS total_duration
    FROM outgoing_calls
    GROUP BY worker_name  
    UNION ALL
    SELECT worker_id, SUM(call_duration) AS total_duration
    FROM income_calls
    GROUP BY worker_name
) AS combined_calls
GROUP BY worker_id
HAVING SUM(total_duration) > 100;

