
def next_cell(cell, direction):
    n, m = len(maze), len(maze[0])
    x, y = cell
    if direction == "L":
        if y > 0 and maze[x][y-1] != "*":
            return (x, y-1)
    elif direction == "R":
        if y < m-1 and maze[x][y+1] != "*":
            return (x, y+1)
    elif direction == "U":
        if x > 0 and maze[x-1][y] != "*":
            return (x-1, y)
    elif direction == "D":
        if x < n-1 and maze[x+1][y] != "*":
            return (x+1, y)
    return None

def find_path(cell, path, k):
    if len(path) == k:
        if cell == start:
            return path
        return None
    
    for direction in ["L", "R", "U", "D"]:
        next_cell_pos = next_cell(cell, direction)
        if next_cell_pos is not None:
            new_path = find_path(next_cell_pos, path+direction, k)
            if new_path is not None:
                return new_path
    
    return None
    
n, m, k = map(int, input().split())
maze = [input() for _ in range(n)]
start = None
for i in range(n):
    for j in range(m):
        if maze[i][j] == "X":
            start = (i, j)
path = find_path(start, "", k)
if path is None:
    print("IMPOSSIBLE")
else:
    print(path)

