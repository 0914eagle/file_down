
def is_valid_move(row, col, visited, N, M):
    if row < 0 or row >= N or col < 0 or col >= M:
        return False
    if (row, col) in visited:
        return False
    return True

def find_tour(N, M):
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    visited = set()
    grid = [[0 for _ in range(M)] for _ in range(N)]
    row, col = 0, 0
    visited.add((row, col))
    grid[row][col] = 1

    for i in range(2, N * M + 1):
        next_move = None
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(new_row, new_col, visited, N, M):
                next_move = (new_row, new_col)
                break
        if next_move is None:
            return -1
        row, col = next_move
        visited.add((row, col))
        grid[row][col] = i

    return grid

N, M = map(int, input().split())
result = find_tour(N, M)
if result == -1:
    print(-1)
else:
    for row in result:
        for col in row:
            print(row, col)
