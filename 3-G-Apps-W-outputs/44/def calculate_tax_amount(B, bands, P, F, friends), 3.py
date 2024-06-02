
def calculate_tax_amount(B, bands, P, F, friends):
    def calculate_tax(income):
        tax = 0
        for i in range(B):
            if i == B - 1:
                tax += (income - bands[i][0]) * bands[i][1] / 100
            else:
                tax += min(income, bands[i][0]) * bands[i][1] / 100
        tax += max(0, income - bands[-1][0]) * P / 100
        return tax

    results = []
    for friend in friends:
        earned, target = friend
        left = target + calculate_tax(earned)
        results.append(left)

    return results

# Input
B = int(input())
bands = [list(map(float, input().split())) for _ in range(B)]
P = float(input())
F = int(input())
friends = [list(map(float, input().split())) for _ in range(F)]

# Calculate and output results
results = calculate_tax_amount(B, bands, P, F, friends)
for result in results:
    print("{:.6f}".format(result))
