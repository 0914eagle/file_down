
import numpy as np

def expected_grade(a, b, c, t):
    return a*t**2 + b*t + c

def max_average_grade(N, T, subjects):
    def objective(x):
        total_grade = 0
        for i in range(N):
            total_grade += expected_grade(*subjects[i], x[i])
        return -total_grade/N  # Minimize negative of total grade to maximize average grade

    x0 = [0.0] * N  # Initial guess for time allocation
    bounds = [(0, T)] * N  # Time allocation bounds

    from scipy.optimize import minimize
    res = minimize(objective, x0, bounds=bounds)
    return -res.fun  # Return the maximum average grade

# Input parsing
N, T = map(int, input().split())
subjects = [tuple(map(float, input().split())) for _ in range(N)]

# Call the function to get the result and print it with 10 decimal places
result = max_average_grade(N, T, subjects)
print(f'{result:.10f}')
