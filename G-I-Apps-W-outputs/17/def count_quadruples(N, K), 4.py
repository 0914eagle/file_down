
def count_quadruples(N, K):
    count = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            for c in range(1, N+1):
                for d in range(1, N+1):
                    if a + b - c - d == K and 1 <= a <= N and 1 <= b <= N and 1 <= c <= N and 1 <= d <= N:
                        count += 1
    return count

N, K = map(int, input().split())
print(count_quadruples(N, K))
```
