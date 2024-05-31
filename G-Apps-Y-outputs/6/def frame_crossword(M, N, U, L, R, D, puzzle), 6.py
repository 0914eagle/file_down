
def frame_crossword(M, N, U, L, R, D, puzzle):
    framed_puzzle = []

    top_row = '#' + '.#'*N + '.'
    bottom_row = '.' + '#.'*N + '#'

    for i in range(U):
        framed_puzzle.append(top_row)
    
    for i in range(M):
        row = '#' + '.'*L + puzzle[i] + '.'*R + '#'
        framed_puzzle.append(row)
    
    for i in range(D):
        framed_puzzle.append(bottom_row)

    return framed_puzzle

# Input
M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
puzzle = [input() for _ in range(M)]

# Output
framed_puzzle = frame_crossword(M, N, U, L, R, D, puzzle)
for row in framed_puzzle:
    print(row)

