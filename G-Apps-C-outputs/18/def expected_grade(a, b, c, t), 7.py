
import sys

def expected_grade(a, b, c, t):
    return a * t**2 + b * t + c

def maximize_average_grade(N, T, subjects):
    def search(l, r):
        for _ in range(100):
            m1 = l + (r - l) / 3
            m2 = r - (r - l) / 3
            if calculate_average_grade(m1) < calculate_average_grade(m2):
                l = m1
            else:
                r = m2
        return calculate_average_grade((l + r) / 2)
    
    def calculate_average_grade(t):
        total_grade = 0
        for a, b, c in subjects:
            total_grade += expected_grade(a, b, c, t)
        return total_grade / N
    
    return search(0, T)

# Read input
N, T = map(int, input().split())
subjects = []
for _ in range(N):
    a, b, c = map(float, input().split())
    subjects.append((a, b, c))

# Calculate and print the result
result = maximize_average_grade(N, T, subjects)
print("{:.10f}".format(result))
