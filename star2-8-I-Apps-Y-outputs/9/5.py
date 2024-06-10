
def spreadWater(grid, N, M):
    newGrid = [["." for i in range(M)] for j in range(N)]
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "V":
                newGrid[i][j] = "V"
            elif grid[i][j] == "#":
                newGrid[i][j] = "#"
            else:
                if i > 0 and grid[i-1][j] == "V":
                    newGrid[i][j] = "V"
                elif i > 0 and j > 0 and grid[i-1][j-1] == "V":
                    newGrid[i][j] = "V"
                elif i > 0 and j < M-1 and grid[i-1][j+1] == "V":
                    newGrid[i][j] = "V"
                else:
                    newGrid[i][j] = "."
    return newGrid

def printGrid(grid, N, M):
    for i in range(N):
        print("".join(grid[i]))

N, M = map(int, input().split())
grid = [list(input()) for i in range(N)]
while True:
    newGrid = spreadWater(grid, N, M)
    if newGrid == grid:
        break
    grid = newGrid
printGrid(grid, N, M)

