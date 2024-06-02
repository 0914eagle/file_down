
def min_days_to_achieve_dream(n, p, q, projects):
    def days_to_achieve_target(x, y):
        if x == 0:
            return float('inf')
        return max((p - x) / a for a, b in projects if a > 0 and b >= y)

    min_days = min(days_to_achieve_target(*target) for target in [(p, q), (0, 0)])
    return min_days

# Read input
n, p, q = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
result = min_days_to_achieve_dream(n, p, q, projects)
print("{:.15f}".format(result))
