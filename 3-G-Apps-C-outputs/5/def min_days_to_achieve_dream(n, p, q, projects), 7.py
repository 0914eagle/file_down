
def min_days_to_achieve_dream(n, p, q, projects):
    def check_days(days):
        total_exp = 0
        total_money = 0
        for a, b in projects:
            exp = a * days
            money = b * days
            total_exp += exp
            total_money += money
        return total_exp >= p and total_money >= q

    left = 0
    right = 10**9
    while right - left > 1e-6:
        mid = (left + right) / 2
        if check_days(mid):
            right = mid
        else:
            left = mid

    return right

# Input parsing
n, p, q = map(int, input().split())
projects = [list(map(int, input().split())) for _ in range(n)]

result = min_days_to_achieve_dream(n, p, q, projects)
print("{:.15f}".format(result))
