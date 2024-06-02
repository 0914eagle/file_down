
def calculate_tax_amount(B, bands, P, F, friends):
    def calculate_tax(income):
        tax = 0
        for i in range(B):
            if i == B - 1:
                tax += (income - bands[i][0]) * bands[i][1] / 100
            else:
                if income > bands[i][0]:
                    tax += (min(income, bands[i+1][0]) - bands[i][0]) * bands[i][1] / 100
        if income > bands[-1][0]:
            tax += (income - bands[-1][0]) * P / 100
        return tax

    results = []
    for friend in friends:
        earned, should_receive = friend
        low = 0
        high = max(earned, should_receive)
        while high - low > 1e-6:
            mid = (low + high) / 2
            tax = calculate_tax(mid)
            if earned - tax < should_receive:
                high = mid
            else:
                low = mid
        results.append(round(low, 6))

    return results

# Input parsing
B = int(input())
bands = []
for _ in range(B):
    s, p = map(float, input().split())
    bands.append((s, p))
P = float(input())
F = int(input())
friends = []
for _ in range(F):
    e, m = map(float, input().split())
    friends.append((e, m))

# Calculate and print results
results = calculate_tax_amount(B, bands, P, F, friends)
for result in results:
    print(result)
