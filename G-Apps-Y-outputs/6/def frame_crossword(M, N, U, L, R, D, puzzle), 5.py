
def frame_crossword(M, N, U, L, R, D, puzzle):
    framed_puzzle = []
    top_bottom_frame = ['#' if i % 2 == 0 else '.' for i in range(N + L + R)]
    middle_frame = ['#' if i % 2 == 0 else '.' for i in range(N)]
    
    for _ in range(U):
        framed_puzzle.append(''.join(top_bottom_frame))
    
    for row in puzzle:
        framed_row = ['#' if i % 2 == 0 else '.' for i in range(L)] + list(row) + ['#' if i % 2 == 0 else '.' for i in range(R)]
        framed_puzzle.append(''.join(framed_row))
    
    for _ in range(D):
        framed_puzzle.append(''.join(top_bottom_frame))
    
    return framed_puzzle

# Input parsing
M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
puzzle = [input() for _ in range(M)]

framed_puzzle = frame_crossword(M, N, U, L, R, D, puzzle)
for row in framed_puzzle:
    print(row)
