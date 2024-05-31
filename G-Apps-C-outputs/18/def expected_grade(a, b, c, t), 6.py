
import itertools

def expected_grade(a, b, c, t):
    return a*t**2 + b*t + c

def max_average_grade(N, T, subjects):
    max_average = 0.0
    
    for allocation in itertools.product(range(T+1), repeat=N):
        total_time = sum(allocation)
        if total_time <= T:
            average_grade = sum([expected_grade(*subject, t) for subject, t in zip(subjects, allocation)]) / N
            max_average = max(max_average, average_grade)
    
    return round(max_average, 10)

# Input parsing
N, T = map(int, input().split())
subjects = [list(map(float, input().split())) for _ in range(N)]

# Calculate and output the maximum average grade
print(max_average_grade(N, T, subjects))
