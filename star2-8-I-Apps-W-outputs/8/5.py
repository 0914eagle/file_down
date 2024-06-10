
def count_triplets(grid):
    N = len(grid)
    triplets = 0
    for row in range(N):
        for col in range(N):
            letter = grid[row][col]
            if letter != '.':
                for x in range(col + 1, N):
                    if grid[row][x] == letter:
                        for y in range(row + 1, N):
                            if grid[y][x] == letter:
                                triplets += 1
                                break
                    else:
                        break
    return triplets

N = int(input())
grid = [input() for _ in range(N)]
triplets = count_triplets(grid)
print(triplets)

