
def distribute_crackers(N, K):
    minimum_difference = abs(N // K * K - N)
    return minimum_difference

# Input
N, K = map(int, input().split())

# Output
print(distribute_crackers(N, K))
```
