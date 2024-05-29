
def find_minimum_amount(N, K, D):
    while True:
        if all(digit not in str(N) for digit in D):
            return N
        N += 1

# Reading input
N, K = map(int, input().split())
D = list(map(int, input().split()))

# Finding and printing the minimum amount
result = find_minimum_amount(N, K, D)
print(result)
```
