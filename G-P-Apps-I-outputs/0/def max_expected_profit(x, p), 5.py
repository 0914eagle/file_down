
def max_expected_profit(x, p):
    if p >= 50:
        return 0.0
    
    # Calculate the expected profit for each bet
    expected_profit_per_bet = (1 - p*2) + p*(1 + ((100-x)/100)*2)
    
    # Determine the maximum number of bets to place
    max_bets = 1 / expected_profit_per_bet
    
    # Calculate the maximum expected profit
    max_profit = max_bets * expected_profit_per_bet
    
    return round(max_profit, 3)

# Input
x, p = map(float, input().split())

# Output
print(max_expected_profit(x, p))
```
