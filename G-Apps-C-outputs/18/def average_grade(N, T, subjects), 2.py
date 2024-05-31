
import sys

def average_grade(N, T, subjects):
    def calculate_grade(a, b, c, t):
        return a * t**2 + b * t + c

    def binary_search(subjects, lo, hi, T):
        while hi - lo > 1e-6:
            mid = (lo + hi) / 2
            total_grade = sum(max(0, calculate_grade(a, b, c, min(mid, T))) for a, b, c in subjects)
            if total_grade >= 100 * N:
                hi = mid
            else:
                lo = mid
        return lo

    lo = 0
    hi = 100
    max_grade = binary_search(subjects, lo, hi, T)
    return max_grade

if __name__ == "__main__":
    N, T = map(int, sys.stdin.readline().strip().split())
    subjects = []
    for _ in range(N):
        a, b, c = map(float, sys.stdin.readline().strip().split())
        subjects.append((a, b, c))
    
    result = average_grade(N, T, subjects)
    print("{:.10f}".format(result))
