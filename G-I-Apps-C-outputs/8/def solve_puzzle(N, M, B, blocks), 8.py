
def solve_puzzle(N, M, B, blocks):
    initial_board = [[0 for _ in range(M)] for _ in range(N)]
    for r, c in blocks:
        initial_board[r-1][c-1] = 1
    
    target_board = [[0 for _ in range(M)] for _ in range(N)]
    for r, c in blocks:
        target_board[r-1][c-1] = 1

    moves = []
    for i in range(N):
        for j in range(M):
            if initial_board[i][j] != target_board[i][j]:
                if i == N-1:
                    moves.append(('v', j+1))
                else:
                    moves.append(('^', i+1))
                    moves.append(('<', j+1))
                    initial_board[i][j] = 1

    if initial_board == target_board:
        print("possible")
        for move in moves:
            print(move[0], move[1])
    else:
        print("impossible")

# Input parsing
N, M, B = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(B)]

# Solve the puzzle
solve_puzzle(N, M, B, blocks)
```
