
def min_days_to_achieve_dream(n, p, q, projects):
    def check_days(days):
        total_exp = 0
        total_money = 0
        for i in range(n):
            exp_per_day, money_per_day = projects[i]
            exp_gain = exp_per_day * days
            money_gain = money_per_day * days
            total_exp = max(total_exp, exp_gain)
            total_money = max(total_money, money_gain)
        return total_exp >= p and total_money >= q

    left = 0
    right = 10**18
    while right - left > 1e-6:
        mid = (left + right) / 2
        if check_days(mid):
            right = mid
        else:
            left = mid

    return right

# Input parsing
n, p, q = map(int, input().split())
projects = []
for _ in range(n):
    a, b = map(int, input().split())
    projects.append((a, b))

# Call the function and print the output
result = min_days_to_achieve_dream(n, p, q, projects)
print("{:.15f}".format(result))
