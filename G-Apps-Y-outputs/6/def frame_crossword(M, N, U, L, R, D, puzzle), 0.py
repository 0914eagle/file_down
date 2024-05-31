
def frame_crossword(M, N, U, L, R, D, puzzle):
    framed_puzzle = []
    
    for i in range(M + U + D):
        row = ""
        for j in range(N + L + R):
            if i < U or i >= M + U or j < L or j >= N + L:
                if (i+j) % 2 == 0:
                    row += "#"
                else:
                    row += "."
            else:
                row += puzzle[i-U][j-L]
        framed_puzzle.append(row)
    
    return framed_puzzle

# Input processing
M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
puzzle = [input().strip() for _ in range(M)]

# Output framed crossword puzzle
framed_puzzle = frame_crossword(M, N, U, L, R, D, puzzle)
for row in framed_puzzle:
    print(row)
