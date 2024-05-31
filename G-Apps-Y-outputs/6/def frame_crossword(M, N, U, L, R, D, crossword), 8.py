
def frame_crossword(M, N, U, L, R, D, crossword):
    framed_crossword = [['#' if (i+j) % 2 == 0 else '.' for j in range(N+U+L+R)] for i in range(M+U+D)]
    
    for i in range(U, U+M):
        for j in range(L, L+N):
            framed_crossword[i][j] = crossword[i-U][j-L]
    
    for row in framed_crossword:
        print(''.join(row))

# Read input
M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
crossword = [list(input().strip()) for _ in range(M)]

# Frame crossword puzzle
frame_crossword(M, N, U, L, R, D, crossword)
