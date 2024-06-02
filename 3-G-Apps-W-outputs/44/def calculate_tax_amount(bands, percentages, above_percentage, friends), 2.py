
def calculate_tax_amount(bands, percentages, above_percentage, friends):
    def calculate_tax(income):
        tax = 0
        for i in range(bands):
            if income > percentages[i][0]:
                tax += (percentages[i][0] - max(0, percentages[i-1][0])) * percentages[i][1] / 100
            else:
                tax += (income - max(0, percentages[i-1][0])) * percentages[i][1] / 100
                break
        tax += max(0, income - percentages[-1][0]) * above_percentage / 100
        return tax

    results = []
    for friend in friends:
        earned, target = friend
        low, high = 0, earned
        while high - low > 1e-6:
            mid = (low + high) / 2
            if calculate_tax(mid) > earned - target:
                high = mid
            else:
                low = mid
        results.append(format(low, '.6f'))

    return results

# Input
bands = int(input())
percentages = [list(map(float, input().split())) for _ in range(bands)]
above_percentage = float(input())
num_friends = int(input())
friends = [list(map(float, input().split())) for _ in range(num_friends)]

# Output
results = calculate_tax_amount(bands, percentages, above_percentage, friends)
for result in results:
    print(result)
