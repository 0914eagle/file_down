
def min_days_to_achieve_dream(n, p, q, projects):
    def check_days(days):
        min_exp = float('inf')
        for a, b in projects:
            min_exp = min(min_exp, a * days + b)
        return min_exp >= p * days and sum(a * days + b for a, b in projects) >= q * days

    left, right = 0, 10**9
    for _ in range(100):
        mid = (left + right) / 2
        if check_days(mid):
            right = mid
        else:
            left = mid

    return right

# Input parsing
n, p, q = map(int, input().split())
projects = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the output
result = min_days_to_achieve_dream(n, p, q, projects)
print("{:.15f}".format(result))
