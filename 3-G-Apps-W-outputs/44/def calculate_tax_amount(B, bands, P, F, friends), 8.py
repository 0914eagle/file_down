
def calculate_tax_amount(B, bands, P, F, friends):
    def calculate_tax(income):
        tax = 0
        for i in range(B):
            if income <= bands[i][0]:
                tax += income * bands[i][1] / 100
                return tax
            else:
                tax += bands[i][0] * bands[i][1] / 100
                income -= bands[i][0]
        tax += income * P / 100
        return tax

    results = []
    for friend in friends:
        earned, target = friend
        low = 0
        high = earned
        while high - low > 1e-6:
            mid = (low + high) / 2
            tax_paid = calculate_tax(mid)
            net_amount = mid - tax_paid
            if net_amount < target:
                low = mid
            else:
                high = mid
        results.append(format(low, '.6f'))

    return results

# Input parsing
B = int(input())
bands = [list(map(float, input().split())) for _ in range(B)]
P = float(input())
F = int(input())
friends = [list(map(float, input().split())) for _ in range(F)]

# Calculate and output results
results = calculate_tax_amount(B, bands, P, F, friends)
for result in results:
    print(result)
