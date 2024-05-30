
def calculate_expected_profit(x, p):
    expected_profit = 2 * p - (1 - p) * (1 + x/100)
    return round(expected_profit, 3)

# Input
x, p = map(float, input().split())

# Calculate and output the maximum expected profit
print(calculate_expected_profit(x, p))
