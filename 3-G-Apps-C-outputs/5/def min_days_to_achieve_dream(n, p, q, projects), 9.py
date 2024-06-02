
def min_days_to_achieve_dream(n, p, q, projects):
    def check_days(days):
        min_exp = float('inf')
        for a, b in projects:
            exp_needed = max(0, p - a * days)
            money_needed = max(0, q - b * days)
            min_exp = min(min_exp, exp_needed / a + money_needed / b)
        return min_exp

    left = 0
    right = max(p / a for a, _ in projects + [(1, 1)]) + max(q / b for _, b in projects + [(1, 1)])
    for _ in range(100):
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        if check_days(mid1) < check_days(mid2):
            right = mid2
        else:
            left = mid1

    return check_days(left)

# Input parsing
n, p, q = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Call the function and print the result
result = min_days_to_achieve_dream(n, p, q, projects)
print("{:.15f}".format(result))
