
def solve_sliding_blocks(N, M, B, blocks):
    initial_board = [[0]*M for _ in range(N)]
    for r, c in blocks:
        initial_board[r-1][c-1] = 1

    target_board = [[0]*M for _ in range(N)]
    for r, c in blocks:
        target_board[r-1][c-1] = 1

    moves = []
    for r in range(1, N):
        moves.append(("v", r))
    for r in range(N-2, -1, -1):
        moves.append(("^", r))

    for c in range(1, M):
        moves.append(("<", c))
    for c in range(M-2, -1, -1):
        moves.append((">", c))

    for move in moves:
        direction, pos = move
        if direction == "v":
            for i in range(N):
                if initial_board[i][pos] == 0:
                    initial_board[i][pos] = 1
                    break
        elif direction == "^":
            for i in range(N-1, -1, -1):
                if initial_board[i][pos] == 0:
                    initial_board[i][pos] = 1
                    break
        elif direction == "<":
            for i in range(M):
                if initial_board[pos][i] == 0:
                    initial_board[pos][i] = 1
                    break
        elif direction == ">":
            for i in range(M-1, -1, -1):
                if initial_board[pos][i] == 0:
                    initial_board[pos][i] = 1
                    break

    if initial_board == target_board:
        print("possible")
        for move in moves:
            print(move[0], move[1]+1)
    else:
        print("impossible")

# Input parsing
N, M, B = map(int, input().split())
blocks = [tuple(map(int, input().split())) for _ in range(B)]

solve_sliding_blocks(N, M, B, blocks)
```
