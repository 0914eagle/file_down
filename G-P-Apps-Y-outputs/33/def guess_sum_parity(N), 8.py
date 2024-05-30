
def guess_sum_parity(N):
    if N % 2 == 0:
        return 'Even'
    else:
        return 'Either'

# Taking input for N
N = int(input())
result = guess_sum_parity(N)
print(result)
```
