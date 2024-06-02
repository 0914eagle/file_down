
def calculate_tax_amount(B, bands, P, F, friends):
    def calculate_tax(income):
        tax = 0
        for i in range(B):
            if i == B - 1:
                tax += (income - bands[i][0]) * bands[i][1] / 100
            else:
                tax += min(income, bands[i][0]) * bands[i][1] / 100
        return tax + (income - bands[-1][0]) * P / 100

    result = []
    for friend in friends:
        earned, target = friend
        low, high = 0, 2 * target
        while high - low > 1e-6:
            mid = (low + high) / 2
            tax = calculate_tax(mid)
            if tax > earned:
                high = mid
            else:
                low = mid
        result.append(round(low, 6))

    return result

# Input parsing
B = int(input())
bands = [list(map(float, input().split())) for _ in range(B)]
P = float(input())
F = int(input())
friends = [list(map(float, input().split())) for _ in range(F)]

# Calculate and print the result
result = calculate_tax_amount(B, bands, P, F, friends)
for res in result:
    print(res)
