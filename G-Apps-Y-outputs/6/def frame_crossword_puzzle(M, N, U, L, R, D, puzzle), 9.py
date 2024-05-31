
def frame_crossword_puzzle(M, N, U, L, R, D, puzzle):
    framed_puzzle = []
    
    # Create the top frame
    top_frame = '#' + '.#'*N + '.'*R
    for _ in range(U):
        framed_puzzle.append(top_frame)
    
    # Create the puzzle with left and right frames
    for row in puzzle:
        framed_row = '#' + '.'.join(row) + '.'*R
        for _ in range(L):
            framed_puzzle.append(framed_row)
    
    # Create the bottom frame
    bottom_frame = '#' + '.#'*N + '.'*R
    for _ in range(D):
        framed_puzzle.append(bottom_frame)
    
    return framed_puzzle

# Read input
M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
puzzle = [input() for _ in range(M)]

# Frame the crossword puzzle
framed_puzzle = frame_crossword_puzzle(M, N, U, L, R, D, puzzle)

# Output the framed crossword puzzle
for row in framed_puzzle:
    print(row)

