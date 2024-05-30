
def solve_sliding_blocks(N, M, B, blocks):
    initial_board = [[False for _ in range(M)] for _ in range(N)]
    for block in blocks:
        initial_board[block[0]-1][block[1]-1] = True

    target_board = [[False for _ in range(M)] for _ in range(N)]
    for block in blocks[1:]:
        target_board[block[0]-1][block[1]-1] = True

    moves = []
    for r in range(N):
        for c in range(M):
            if initial_board[r][c] and not target_board[r][c]:
                if r < N-1:
                    moves.append(('^', r+1))
                    initial_board[r][c] = False
                    initial_board[r+1][c] = True
                elif c < M-1:
                    moves.append(('<', c+1))
                    initial_board[r][c] = False
                    initial_board[r][c+1] = True
                else:
                    return "impossible"

    return "possible", moves

# Read input
N, M, B = map(int, input().split())
blocks = [tuple(map(int, input().split())) for _ in range(B)]

# Solve and output
result = solve_sliding_blocks(N, M, B, blocks)
if result == "impossible":
    print("impossible")
else:
    print("possible")
    for move in result[1]:
        print(move[0], move[1])
```
