
def frame_crossword(M, N, U, L, R, D, crossword):
    framed_crossword = []
    
    for i in range(M + U + D):
        row = ""
        for j in range(N + L + R):
            if (i+j) % 2 == 0:
                row += "#"
            else:
                row += "."
        framed_crossword.append(row)
    
    for i in range(M):
        for j in range(N):
            framed_crossword[i+U][j+L] = crossword[i][j]
    
    for row in framed_crossword:
        print(row)
    
# Input
M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
crossword = []
for _ in range(M):
    crossword.append(input().strip())
    
# Frame the crossword puzzle
frame_crossword(M, N, U, L, R, D, crossword)
