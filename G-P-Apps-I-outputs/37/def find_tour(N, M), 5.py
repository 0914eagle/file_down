
def find_tour(N, M):
    if N * M % 2 == 1:
        return -1
    
    tour = []
    for i in range(1, N+1):
        for j in range(1, M+1):
            if (i + j) % 2 == 0:
                tour.append((i, j))
    
    if N % 2 == 1:
        for j in range(1, M+1):
            if j % 2 == 1:
                tour.append((N, j))
            else:
                tour.append((N-1, j))
    return tour

# Input
N, M = map(int, input().split())

# Output
result = find_tour(N, M)
if result == -1:
    print(-1)
else:
    for row, col in result:
        print(row, col)
```
