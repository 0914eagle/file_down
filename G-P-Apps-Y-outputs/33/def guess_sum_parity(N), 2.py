
def guess_sum_parity(N):
    if N % 2 == 0 or (N == 1 and N % 2 == 0):
        return 'Even'
    elif N % 2 != 0:
        return 'Odd'
    else:
        return 'Either'

# Test the function with the sample input
N = 1
print(guess_sum_parity(N))
```
