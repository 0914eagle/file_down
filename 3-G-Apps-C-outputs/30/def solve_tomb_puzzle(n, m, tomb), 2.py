
def solve_tomb_puzzle(n, m, tomb):
    def is_valid_position(x, y):
        return 0 <= x < n and 0 <= y < m

    def is_mirror(char):
        return char == '/' or char == '\\'

    def rotate_gargoyle(char):
        if char == 'V':
            return 'H'
        elif char == 'H':
            return 'V'
        else:
            return char

    def can_reach_treasure(start_x, start_y, direction):
        visited = set()
        x, y = start_x, start_y

        while is_valid_position(x, y):
            if (x, y) in visited:
                return False

            visited.add((x, y))

            if tomb[x][y] == '#':
                return False

            if tomb[x][y] == 'V' or tomb[x][y] == 'H':
                if (x, y) != (start_x, start_y):
                    return False

            if tomb[x][y] == '/':
                if direction == 'up':
                    direction = 'right'
                elif direction == 'down':
                    direction = 'left'
                elif direction == 'left':
                    direction = 'down'
                else:
                    direction = 'up'

            elif tomb[x][y] == '\\':
                if direction == 'up':
                    direction = 'left'
                elif direction == 'down':
                    direction = 'right'
                elif direction == 'left':
                    direction = 'up'
                else:
                    direction = 'down'

            if direction == 'up':
                x -= 1
            elif direction == 'down':
                x += 1
            elif direction == 'left':
                y -= 1
            else:
                y += 1

            if (x, y) == (start_x, start_y):
                return True

        return False

    gargoyle_count = 0

    for i in range(n):
        for j in range(m):
            if tomb[i][j] == 'V' or tomb[i][j] == 'H':
                if can_reach_treasure(i, j, 'up') or can_reach_treasure(i, j, 'down') or can_reach_treasure(i, j, 'left') or can_reach_treasure(i, j, 'right'):
                    continue
                else:
                    tomb[i][j] = rotate_gargoyle(tomb[i][j])
                    gargoyle_count += 1

    return gargoyle_count if gargoyle_count <= (n*m) // 2 else -1

# Input
n, m = map(int, input().split())
tomb = [list(input()) for _ in range(n)]

# Output
print(solve_tomb_puzzle(n, m, tomb))
