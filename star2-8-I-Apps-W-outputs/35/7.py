
def solve():
    mat = [input() for i in range(4)]
    if any(mat[i][j] == mat[i][j+1] == mat[i+1][j] == mat[i+1][j+1] for i in range(3) for j in range(3)):
        print("YES")
    else:
        print("NO")
solve()

