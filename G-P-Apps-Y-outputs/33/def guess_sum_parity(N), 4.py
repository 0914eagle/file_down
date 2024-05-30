
def guess_sum_parity(N):
    if N % 2 == 0 or (N == 1 and N != 100):
        return 'Even'
    elif N == 1 or N == 100:
        return 'Either'
    else:
        return 'Odd'

# Input
N = int(input())

# Output
result = guess_sum_parity(N)
print(result)
```
