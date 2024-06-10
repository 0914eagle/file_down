
def solve(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                start = (i, j)
                break
    queue = [(start, 0)]
    visited = set()
    while queue:
        pos, steps = queue.pop(0)
        if pos == (0, 0):
            return steps
        if pos in visited:
            continue
        visited.add(pos)
        for r, c in [(pos[0] + 2, pos[1] + 1), (pos[0] + 2, pos[1] - 1), (pos[0] - 2, pos[1] + 1), (pos[0] - 2, pos[1] - 1), (pos[0] + 1, pos[1] + 2), (pos[0] + 1, pos[1] - 2), (pos[0] - 1, pos[1] + 2), (pos[0] - 1, pos[1] - 2)]:
            if 0 <= r < n and 0 <= c < n and board[r][c] != '#' and (r, c) not in visited:
                queue.append(((r, c), steps + 1))
    return -1

if __name__ == '__main__':
    n = int(input())
    board = [input() for _ in range(n)]
    print(solve(board))

