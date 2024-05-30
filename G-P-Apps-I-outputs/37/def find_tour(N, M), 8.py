
def find_tour(N, M):
    if N % 2 == 1 and M % 2 == 1:
        return -1
    
    grid = [[0 for _ in range(M)] for _ in range(N)]
    row = 0
    col = 0
    count = 1

    for i in range(N):
        for j in range(M):
            grid[i][j] = (row + 1, col + 1)
            count += 1
            if count % 2 == 0:
                row = (row + 1) % N
            else:
                col = (col + 1) % M

    return grid

# Sample Input
N, M = map(int, input().split())
result = find_tour(N, M)

if result == -1:
    print(-1)
else:
    for row in result:
        for col in row:
            print(col[0], col[1])
