
def count_quadruples(N, K):
    count = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            for c in range(1, N+1):
                for d in range(1, N+1):
                    if a + b - c - d == K:
                        count += 1
    return count

# Read input from standard input
N, K = map(int, input().split())

# Calculate and print the number of quadruples satisfying the conditions
print(count_quadruples(N, K))
```
