
def distribute_crackers(N, K):
    min_diff = N % K
    return min_diff

N, K = map(int, input().split())
result = distribute_crackers(N, K)
print(result)
```
