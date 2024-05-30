
def solve_tomb_puzzle(n, m, floorplan):
    def can_direct_light(row, col, direction):
        if 0 <= row < n and 0 <= col < m:
            if floorplan[row][col] == '.':
                return can_direct_light(row + direction[0], col + direction[1], direction)
            elif floorplan[row][col] == 'V':
                return direction in [(1, 0), (-1, 0)]
            elif floorplan[row][col] == 'H':
                return direction in [(0, 1), (0, -1)]
            else:
                return False
        return False
    
    def rotate_gargoyle(row, col):
        nonlocal rotated_gargoyles
        if floorplan[row][col] == 'V':
            rotated_gargoyles.add((row, col))
            floorplan[row][col] = 'H'
        elif floorplan[row][col] == 'H':
            rotated_gargoyles.add((row, col))
            floorplan[row][col] = 'V'
    
    rotated_gargoyles = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for i in range(n):
        for j in range(m):
            if floorplan[i][j] == 'V' or floorplan[i][j] == 'H':
                for direction in directions:
                    new_row, new_col = i + direction[0], j + direction[1]
                    if can_direct_light(new_row, new_col, direction) and (new_row, new_col) not in rotated_gargoyles:
                        rotate_gargoyle(i, j)
                        break
    
    for i in range(n):
        for j in range(m):
            if floorplan[i][j] == 'V' or floorplan[i][j] == 'H':
                return -1
    
    return len(rotated_gargoyles)

# Read input
n, m = map(int, input().split())
floorplan = [input() for _ in range(n)]

# Call the function and print the result
print(solve_tomb_puzzle(n, m, floorplan))
```
