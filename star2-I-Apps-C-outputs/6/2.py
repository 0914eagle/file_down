
def solve(B, H, R, C, grid):
    def light_level(x, y, z, s):
        return s / (x**2 + y**2 + z**2)
    total_cost = 0
    for r in range(R):
        for c in range(C):
            s = int(grid[r][c])
            if s < B:
                total_cost += 11
            else:
                total_cost += 43
    return total_cost

