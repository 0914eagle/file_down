
def calculate_expected_profit(x, p):
    if p >= 50:
        return 0.0
    
    # Calculate expected profit
    expected_loss = x / 100
    expected_win = p / 100

    expected_profit = expected_win - expected_loss
    return max(0, expected_profit)

# Input
x, p = map(float, input().split())

# Calculate and output the maximum expected profit
print("{:.3f}".format(calculate_expected_profit(x, p)))
