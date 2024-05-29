
def distribute_crackers(N, K):
    if N % K == 0:
        return 0
    else:
        return min(N % K, K - N % K)

# Taking input from Standard Input
N, K = map(int, input().split())

# Calling the function and printing the output
print(distribute_crackers(N, K))
```
