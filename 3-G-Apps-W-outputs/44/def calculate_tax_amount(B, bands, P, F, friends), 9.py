
def calculate_tax_amount(B, bands, P, F, friends):
    def calculate_tax(income):
        tax = 0
        for i in range(B):
            if i == B - 1:
                tax += (income - bands[i][0]) * bands[i][1] / 100
            else:
                tax += min(income, bands[i][0]) * bands[i][1] / 100
        if income > bands[-1][0]:
            tax += (income - bands[-1][0]) * P / 100
        return tax

    result = []
    for friend in friends:
        earned, target = friend
        left = target + calculate_tax(earned)
        result.append(left)

    return result

# Input
B = int(input())
bands = [list(map(float, input().split())) for _ in range(B)]
P = float(input())
F = int(input())
friends = [list(map(float, input().split())) for _ in range(F)]

# Calculate and output
result = calculate_tax_amount(B, bands, P, F, friends)
for amount in result:
    print("{:.6f}".format(amount))
