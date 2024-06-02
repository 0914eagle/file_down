
def calculate_tax_amount(B, bands, P, F, friends):
    def calculate_tax(income):
        tax = 0
        for i in range(B):
            if i == B - 1:
                tax += (income - bands[i][0]) * (bands[i][1] / 100)
            else:
                tax += min(bands[i][0], income) * (bands[i][1] / 100)
        if income > bands[-1][0]:
            tax += (income - bands[-1][0]) * (P / 100)
        return tax

    results = []
    for friend in friends:
        earned, target = friend
        low, high = 0, earned
        while high - low > 1e-6:
            mid = (low + high) / 2
            tax = calculate_tax(mid)
            if tax > earned - target:
                high = mid
            else:
                low = mid
        results.append("{:.6f}".format(low))

    return results

# Input parsing
B = int(input())
bands = [list(map(float, input().split())) for _ in range(B)]
P = float(input())
F = int(input())
friends = [list(map(float, input().split())) for _ in range(F)]

# Calculate and print the results
results = calculate_tax_amount(B, bands, P, F, friends)
for result in results:
    print(result)
