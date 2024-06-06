
def solve(grid):
    N = len(grid)
    i, j = 0, 0
    while grid[i][j] != 'R':
        i += 1
    directions = ['>','v','<','^']
    direction_index = 0
    visited = []
    flag = True
    while flag:
        if grid[i][j] != 'R':
            flag = False
            continue
        else:
            visited.append((i,j))
            grid[i][j] = 'X'
            direction = directions[direction_index]
            if direction == '>':
                j += 1
            elif direction == 'v':
                i += 1
            elif direction == '<':
                j -= 1
            else:
                i -= 1
            if (i,j) in visited:
                return len(visited)
            direction_index += 1
            direction_index %= 4
    return 1

if __name__ == "__main__":
    N = int(input())
    program = input()
    grid = []
    for _ in range(N):
        grid.append(list(input()))
    print(solve(grid))
