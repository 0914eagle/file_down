
def min_days_to_achieve_dream(n, p, q, projects):
    def feasible(days):
        exp_needed = p * days
        money_needed = q * days
        for a, b in projects:
            exp_per_day = a
            money_per_day = b
            if exp_per_day * days >= exp_needed and money_per_day * days >= money_needed:
                return True
        return False

    left = 0
    right = 10**18
    while right - left > 1e-6:
        mid = (left + right) / 2
        if feasible(mid):
            right = mid
        else:
            left = mid

    return right

# Input parsing
n, p, q = map(int, input().split())
projects = [list(map(int, input().split())) for _ in range(n)]

result = min_days_to_achieve_dream(n, p, q, projects)
print("{:.15f}".format(result))
