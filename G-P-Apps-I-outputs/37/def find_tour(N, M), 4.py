
def find_tour(N, M):
    if N * M % 2 != 0:
        print(-1)
        return

    rows = []
    for i in range(1, N+1):
        cols = list(range(1, M+1))
        if i % 2 == 0:
            cols.reverse()
        rows.append(cols)

    for i in range(N):
        for j in range(M):
            if i % 2 == 0:
                print(f"{i+1} {rows[i][j]}")
            else:
                print(f"{i+1} {rows[i][M-j-1]}")

# Input
N, M = map(int, input().split())

# Output
find_tour(N, M)
