
def is_canonical(n, denominations):
    if n < 2:
        return "non-canonical"

    max_denomination = denominations[-1]
    sum_of_two_largest = denominations[-1] + denominations[-2]

    for x in range(1, sum_of_two_largest):
        coins_needed_greedy = 0
        amount_remaining = x

        for i in range(n - 1, -1, -1):
            coins_needed_greedy += amount_remaining // denominations[i]
            amount_remaining %= denominations[i]

        coins_needed_optimal = x
        if coins_needed_greedy > coins_needed_optimal:
            return "non-canonical"

    return "canonical"

# Reading input
n = int(input())
denominations = list(map(int, input().split()))

# Output
print(is_canonical(n, denominations))
```
