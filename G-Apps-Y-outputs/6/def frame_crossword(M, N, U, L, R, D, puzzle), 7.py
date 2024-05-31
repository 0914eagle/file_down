
def frame_crossword(M, N, U, L, R, D, puzzle):
    framed_puzzle = []

    # Create the top frame
    top_frame = ['#' if i % 2 == 0 else '.' for i in range(N + 2*U)]
    framed_puzzle.append(''.join(top_frame))

    # Add the side frames and puzzle content
    for row in range(M):
        framed_row = ['#' if (L + col) % 2 == 0 else '.' for col in range(N + 2*(L+R))]
        framed_row[L:L+N] = puzzle[row]
        framed_puzzle.append(''.join(framed_row))

    # Create the bottom frame
    bottom_frame = ['#' if i % 2 == 0 else '.' for i in range(N + 2*D)]
    framed_puzzle.append(''.join(bottom_frame))

    return framed_puzzle

# Input
M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
puzzle = [input() for _ in range(M)]

# Output
framed_puzzle = frame_crossword(M, N, U, L, R, D, puzzle)
for row in framed_puzzle:
    print(row)
