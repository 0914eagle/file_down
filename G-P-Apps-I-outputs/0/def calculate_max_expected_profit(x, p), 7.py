
def calculate_max_expected_profit(x, p):
    if p >= 50:
        return 0.0
    
    expected_profit = 0
    for i in range(1, 1000):
        total_loss = i - (p/100 * i)
        if total_loss <= 0:
            continue
        
        refund = x/100 * total_loss
        profit = i - total_loss + refund
        expected_profit = max(expected_profit, profit)
    
    return round(expected_profit, 3)

# Input
x, p = map(float, input().split())

# Calculate and output the maximum expected profit
print(calculate_max_expected_profit(x, p))
```
