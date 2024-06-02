
def min_days_to_achieve_dream(n, p, q, projects):
    def check_days(days):
        total_exp = 0
        total_money = 0
        for a, b in projects:
            exp_per_day = a * days
            money_per_day = b * days
            total_exp += exp_per_day
            total_money += money_per_day
        return total_exp >= p and total_money >= q

    left = 0
    right = 10**9  # Set a large upper bound for binary search
    while right - left > 1e-6:
        mid = (left + right) / 2
        if check_days(mid):
            right = mid
        else:
            left = mid

    return round(right, 6)

# Input parsing
n, p, q = map(int, input().split())
projects = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the result
result = min_days_to_achieve_dream(n, p, q, projects)
print(result)
