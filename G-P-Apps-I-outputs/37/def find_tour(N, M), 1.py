
def find_tour(N, M):
    if N * M % 2 == 1:
        return -1
    
    tour = []
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if (i + j) % 2 == 0:
                tour.append((i, j))
    
    return tour

N, M = map(int, input().split())
tour = find_tour(N, M)

if tour == -1:
    print(-1)
else:
    for square in tour:
        print(square[0], square[1])
```
