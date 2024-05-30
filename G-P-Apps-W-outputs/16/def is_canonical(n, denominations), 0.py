
def is_canonical(n, denominations):
    if n <= 2:
        return "canonical"

    counterexample = sum(denominations[-2:]) - 1
    for amount in range(1, counterexample + 1):
        greedy_coins = 0
        remaining_amount = amount
        for coin in reversed(denominations):
            greedy_coins += remaining_amount // coin
            remaining_amount %= coin
        
        optimal_coins = len(denominations)
        if greedy_coins < optimal_coins:
            return "non-canonical"
    
    return "canonical"

# Input processing
n = int(input())
denominations = list(map(int, input().split()))

# Check if the coin system is canonical or non-canonical
result = is_canonical(n, denominations)
print(result)
```
