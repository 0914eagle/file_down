
import numpy as np

def compute_average_grade(N, T, subjects):
    def f(t, a, b, c):
        return a * t**2 + b * t + c

    def compute_max_grade(subject):
        a, b, c = subject
        return (f(T, a, b, c) - f(0, a, b, c)) / T

    max_grades = [compute_max_grade(subject) for subject in subjects]
    return np.mean(max_grades)

# Read input
N, T = map(int, input().split())
subjects = [list(map(float, input().split())) for _ in range(N)]

# Calculate and print the maximum average grade
result = compute_average_grade(N, T, subjects)
print("{:.10f}".format(result))
