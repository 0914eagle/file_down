
import sys

def is_on_line(a, b, c):
    
    return (a[0] - b[0]) * (a[1] - c[1]) == (a[1] - b[1]) * (a[0] - c[0])

def find_triplets(grid):
    
    triplets = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for k in range(i+1, len(grid)):
                for l in range(len(grid[k])):
                    if grid[i][j] != '.' and grid[k][l] != '.' and grid[i][j] == grid[k][l]:
                        for m in range(k+1, len(grid)):
                            for n in range(len(grid[m])):
                                if grid[m][n] != '.' and grid[m][n] == grid[i][j]:
                                    if is_on_line((i, j), (k, l), (m, n)):
                                        triplets += 1
    return triplets

def main():
    n = int(sys.stdin.readline().strip())
    grid = []
    for _ in range(n):
        grid.append(sys.stdin.readline().strip())
    print(find_triplets(grid))

if __name__ == "__main__":
    main()

