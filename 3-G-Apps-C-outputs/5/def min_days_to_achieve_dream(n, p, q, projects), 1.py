
def min_days_to_achieve_dream(n, p, q, projects):
    def check_days(days):
        exp = 0
        money = 0
        for a, b in projects:
            exp += a * min(days, 1)
            money += b * min(days, 1)
            days -= 1
        return exp >= p and money >= q

    left = 0
    right = sum(a for a, _ in projects) + 1
    while right - left > 1e-7:
        mid = (left + right) / 2
        if check_days(mid):
            right = mid
        else:
            left = mid

    return right

# Input parsing
n, p, q = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

result = min_days_to_achieve_dream(n, p, q, projects)
print("{:.15f}".format(result))
