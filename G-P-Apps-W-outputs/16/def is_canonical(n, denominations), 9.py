
def is_canonical(n, denominations):
    counterexample = None
    for x in range(1, denominations[-1] + denominations[-2]):
        coin_count_greedy = 0
        remaining_amount = x
        for i in range(n - 1, -1, -1):
            coin_count_greedy += remaining_amount // denominations[i]
            remaining_amount %= denominations[i]
        coin_count_optimal = x
        if coin_count_greedy != coin_count_optimal:
            counterexample = x
            break
    if counterexample is None:
        return "canonical"
    else:
        return "non-canonical"

# Reading input
n = int(input())
denominations = list(map(int, input().split()))

# Checking if the coin system is canonical or non-canonical
result = is_canonical(n, denominations)
print(result)
```
