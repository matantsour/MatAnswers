# Task 1: Function to simulate grading by chefs with user input
def generate_grades(K, N, J):
    grades = {}
    for contestant in range(1, K+1):
        contestant_grades = []
        print(f"Grading for Contestant {contestant}:")
        for dish in range(1, N+1):
            dish_grades = []
            print(f"  Dish {dish}:")
            for chef in range(1, J+1):
                print(f"    Chef {chef}'s grading:")
                taste = int(input("      Taste score (1-10): "))
                appeal = int(input("      Appeal score (1-10): "))
                execution = int(input("      Execution score (1-10): "))
                dish_grades.append((taste, appeal, execution))
            contestant_grades.append(dish_grades)
        grades[contestant] = contestant_grades
    return grades

# Task 2: Function to calculate averages and return top K/2 contestants
def top_contestants(grades, K):
    averages = {}
    for contestant, dishes in grades.items():
        total_scores = []
        for dish in dishes:
            for chef_grades in dish:
                # Manually calculating the average for each chef's ratings
                avg_score = sum(chef_grades) / len(chef_grades)
                total_scores.append(avg_score)
        # Manually calculating the contestant's overall average
        contestant_avg = sum(total_scores) / len(total_scores)
        averages[contestant] = contestant_avg

    # Sort contestants by average score and return the top K/2
    sorted_contestants = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    top_k_half = sorted_contestants[:K//2]
    return [contestant[0] for contestant in top_k_half]

# Example usage
K = 6  # Number of contestants
N = 3  # Number of dishes per contestant
J = 2  # Number of chefs grading each dish

grades = generate_grades(K, N, J)
print("Grades:", grades)

top_k = top_contestants(grades, K)
print("Top contestants advancing to the next round:", top_k)
