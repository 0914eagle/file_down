
def check(mat):
    for i in range(len(mat)-1):
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] == mat[i][j+1] == mat[i+1][j+1]:
                return "YES"
    return "NO"


mat = []
for i in range(4):
    mat.append(input())
    
print(check(mat))

