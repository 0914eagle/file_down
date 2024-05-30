
def find_tour(N, M):
    if N * M % 2 != 0:
        return -1

    tour = []
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if (i + j) % 2 == 0:
                tour.append((i, j))
    
    for i in range(1, N * M + 1):
        print(tour[i - 1][0], tour[i - 1][1])

N, M = map(int, input().split())
find_tour(N, M)
```
