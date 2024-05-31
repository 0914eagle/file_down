
import itertools

def calculate_grade(a, b, c, t):
    return a * t**2 + b * t + c

def calculate_max_average_grade(N, T, subjects):
    max_average_grade = 0

    for allocations in itertools.product(range(T+1), repeat=N):
        total_time = sum(allocations)
        
        if total_time > T:
            continue

        total_grade = sum(calculate_grade(subjects[i][0], subjects[i][1], subjects[i][2], allocations[i]) for i in range(N))
        average_grade = total_grade / N

        max_average_grade = max(max_average_grade, average_grade)

    return round(max_average_grade, 10)

# Input parsing
N, T = map(int, input().split())
subjects = [list(map(float, input().split())) for _ in range(N)]

# Calculate and print the result
result = calculate_max_average_grade(N, T, subjects)
print(result)
