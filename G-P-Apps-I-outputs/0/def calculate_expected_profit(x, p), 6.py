
def calculate_expected_profit(x, p):
    if p >= 0.5:
        return 0.0
    else:
        return (1 - p) * x - p

# Input
x, p = map(float, input().split())

# Calculate and output the maximum expected profit
print("{:.3f}".format(calculate_expected_profit(x, p)))
