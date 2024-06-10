
def knight_shortest_path(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                start_row, start_col = i, j
                break
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = [(start_row, start_col, 0)]
    visited[start_row][start_col] = True
    while queue:
        row, col, steps = queue.pop(0)
        if row == 0 and col == 0:
            return steps
        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < n and 0 <= new_col < n and not visited[new_row][new_col] and board[new_row][new_col] != '#':
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, steps + 1))
    return -1

n = int(input())
board = [input() for _ in range(n)]
print(knight_shortest_path(board))

