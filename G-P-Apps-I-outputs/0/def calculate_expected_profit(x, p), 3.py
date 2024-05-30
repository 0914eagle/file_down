
def calculate_expected_profit(x, p):
    expected_loss = (1 - p) + p * (1 - x / 100)
    return max(0, 2 * (1 - expected_loss))

# Taking input
x, p = map(float, input().split())

# Calculate and print the maximum expected profit
print("{:.3f}".format(calculate_expected_profit(x, p)))
