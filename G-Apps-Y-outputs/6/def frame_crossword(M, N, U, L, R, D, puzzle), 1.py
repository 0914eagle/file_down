
def frame_crossword(M, N, U, L, R, D, puzzle):
    framed_puzzle = []
    
    top_row = '#' + '.#'*N + '.'
    bottom_row = '#' + '.#'*N + '.'
    
    for _ in range(U):
        framed_puzzle.append(top_row)
    
    for i in range(M):
        row = '#'
        for j in range(L):
            row += '.'
        row += puzzle[i]
        for _ in range(N):
            row += '.'
        for j in range(R):
            row += '.'
        row += '#'
        framed_puzzle.append(row)
    
    for _ in range(D):
        framed_puzzle.append(bottom_row)
    
    return framed_puzzle

# Input parsing
M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
puzzle = [input() for _ in range(M)]

# Output the framed crossword puzzle
framed_puzzle = frame_crossword(M, N, U, L, R, D, puzzle)
for row in framed_puzzle:
    print(row)
