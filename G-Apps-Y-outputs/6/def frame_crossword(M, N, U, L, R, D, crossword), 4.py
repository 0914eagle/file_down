
def frame_crossword(M, N, U, L, R, D, crossword):
    res = []
    for i in range(M + U + D):
        row = ""
        for j in range(N + L + R):
            if (i + j) % 2 == 0:
                row += "#" if (i < U or i >= M + U) or (j < L or j >= N + L) else "."
            else:
                row += "." if (i < U or i >= M + U) or (j < L or j >= N + L) else "#"
        res.append(row)
    
    for i in range(M):
        for j in range(N):
            res[U + i][L + j] = crossword[i][j]
    
    return "\n".join(res)

# Input parsing
M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
crossword = [input() for _ in range(M)]

# Output
framed_crossword = frame_crossword(M, N, U, L, R, D, crossword)
print(framed_crossword)
