
def fence(B, H, R, C, grid):
    total = 0
    for r in range(R):
        for c in range(C):
            s = int(grid[r][c])
            if s < B:
                total += 11
            else:
                total += 43
    return total

B = int(input())
H = int(input())
R, C = map(int, input().split())
grid = [input() for _ in range(R)]
print(fence(B, H, R, C, grid))

