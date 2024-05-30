
def is_canonical_coin_system(n, denominations):
    for i in range(1, denominations[-1] + 1):
        min_coins = [float('inf')] * (i + 1)
        min_coins[0] = 0
        for j in range(1, i + 1):
            for coin in denominations:
                if coin <= j and min_coins[j - coin] + 1 < min_coins[j]:
                    min_coins[j] = min_coins[j - coin] + 1
        if min_coins[i] != min(len(denominations), min_coins[-1]):
            return "non-canonical"
    return "canonical"

n = int(input())
denominations = list(map(int, input().split()))

print(is_canonical_coin_system(n, denominations))
```
