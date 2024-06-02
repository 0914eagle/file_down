
def min_days_to_achieve_dream(n, p, q, projects):
    def check_days(days):
        total_exp = 0
        total_money = 0
        for i in range(n):
            exp_per_day, money_per_day = projects[i]
            exp = min(days * exp_per_day, p - total_exp)
            money = min(days * money_per_day, q - total_money)
            total_exp += exp
            total_money += money
        return total_exp >= p and total_money >= q

    left = 0
    right = max(p / projects[i][0] for i in range(n)) + max(q / projects[i][1] for i in range(n))
    while right - left > 1e-6:
        mid = (left + right) / 2
        if check_days(mid):
            right = mid
        else:
            left = mid

    return "{:.15f}".format(left)

# Input parsing
n, p, q = map(int, input().split())
projects = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the output
print(min_days_to_achieve_dream(n, p, q, projects))
