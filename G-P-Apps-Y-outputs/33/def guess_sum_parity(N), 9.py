
def guess_sum_parity(N):
    if N % 2 == 0 or (N == 1 and N % 2 == 1):
        return 'Odd'
    elif N % 2 == 1:
        return 'Even'
    else:
        return 'Either'

# Test the function with sample input
N = 1
print(guess_sum_parity(N))
```
