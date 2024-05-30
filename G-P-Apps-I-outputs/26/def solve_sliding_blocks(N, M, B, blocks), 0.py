
def solve_sliding_blocks(N, M, B, blocks):
    initial_board = [[0 for _ in range(M)] for _ in range(N)]
    for r, c in blocks:
        initial_board[r-1][c-1] = 1
    
    target_board = [[0 for _ in range(M)] for _ in range(N)]
    for r, c in blocks:
        target_board[r-1][c-1] = 1
    
    def is_possible(board, r, c, direction):
        if direction == '<':
            for col in range(c-2, -1, -1):
                if board[r-1][col] == 1:
                    return False
        elif direction == '>':
            for col in range(c, M):
                if board[r-1][col] == 1:
                    return False
        elif direction == '^':
            for row in range(r-2, -1, -1):
                if board[row][c-1] == 1:
                    return False
        elif direction == 'v':
            for row in range(r, N):
                if board[row][c-1] == 1:
                    return False
        return True
    
    moves = []
    for r, c in blocks[1:]:
        if r == 1:
            if is_possible(initial_board, r, c, 'v'):
                moves.append('v ' + str(c))
            elif is_possible(initial_board, r, c, '^'):
                moves.append('^ ' + str(c))
        elif r == N:
            if is_possible(initial_board, r, c, '^'):
                moves.append('^ ' + str(c))
            elif is_possible(initial_board, r, c, 'v'):
                moves.append('v ' + str(c))
        if c == 1:
            if is_possible(initial_board, r, c, '>'):
                moves.append('> ' + str(r))
            elif is_possible(initial_board, r, c, '<'):
                moves.append('< ' + str(r))
        elif c == M:
            if is_possible(initial_board, r, c, '<'):
                moves.append('< ' + str(r))
            elif is_possible(initial_board, r, c, '>'):
                moves.append('> ' + str(r))
    
    if len(moves) == B-1:
        print("possible")
        for move in moves:
            print(move)
    else:
        print("impossible")

# Input reading
N, M, B = map(int, input().split())
blocks = []
for _ in range(B):
    r, c = map(int, input().split())
    blocks.append((r, c))

# Solve and output
solve_sliding_blocks(N, M, B, blocks)
```
