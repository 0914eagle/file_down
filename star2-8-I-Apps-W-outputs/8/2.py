
def find_triplets(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                for k in range(j+1, len(grid[0])):
                    if grid[i][k] != '.':
                        for l in range(k+1, len(grid[0])):
                            if grid[i][l] != '.':
                                count += 1
    return count
grid = [list(input()) for _ in range(int(input()))]
print(find_triplets(grid))

