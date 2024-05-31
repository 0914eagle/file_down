
def expected_grade(a, b, c, t):
    return a * t**2 + b * t + c

def max_average_grade(N, T, subjects):
    def average_grade(t_values):
        total_grade = sum(expected_grade(*subject, t) for subject, t in zip(subjects, t_values))
        return total_grade / N
    
    def feasible(t_values):
        return all(expected_grade(*subject, t) >= 0 and expected_grade(*subject, t) <= 100 for subject, t in zip(subjects, t_values))
    
    def objective(t_values):
        return -average_grade(t_values)
    
    from scipy.optimize import minimize

    initial_guess = [T / N] * N
    bounds = [(0, T)] * N

    result = minimize(objective, initial_guess, bounds=bounds, constraints={'type': 'eq', 'fun': lambda t: sum(t) - T})
    
    return -result.fun

# Input parsing
N, T = map(int, input().split())
subjects = [list(map(float, input().split())) for _ in range(N)]

# Call the function and print the result
print("{:.10f}".format(max_average_grade(N, T, subjects)))
