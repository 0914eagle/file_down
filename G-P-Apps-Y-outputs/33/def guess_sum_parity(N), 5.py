
def guess_sum_parity(N):
    lowest = sum(range(1, N + 1)) % 2
    highest = sum(range(101 - N, 101)) % 2

    if lowest == highest:
        return 'Either'
    elif lowest % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

# Example Input
N = 1
print(guess_sum_parity(N))
```
