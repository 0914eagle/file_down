
def frame_crossword(M, N, U, L, R, D, puzzle):
    frame = [['#.' * (N + L + R) for _ in range(U)] +
             ['#' + '.'.join(row) + '#' for row in puzzle] +
             ['#.' * (N + L + R) for _ in range(D)]]
    
    return '\n'.join([''.join(row) for row in frame])

# Read input
M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
puzzle = [list(input().strip()) for _ in range(M)]

# Output framed crossword puzzle
print(frame_crossword(M, N, U, L, R, D, puzzle))
