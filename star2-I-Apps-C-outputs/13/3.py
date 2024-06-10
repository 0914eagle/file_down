
def solve(grid, start, end, stamina):
    pass

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    grid = [input() for _ in range(N)]
    start = (0, 0)
    end = (0, 0)
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                end = (i, j)
    print(solve(grid, start, end, K))

