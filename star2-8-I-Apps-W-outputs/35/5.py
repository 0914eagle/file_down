
def isSameColor(cell1, cell2, cell3, cell4):
    if cell1 == cell2 and cell1 == cell3 and cell1 == cell4:
        return True
    
    return False

def isSquare(cell1, cell2, cell3, cell4):
    if cell1 == '.' and cell2 == '.' and cell3 == '.' and cell4 == '.':
        return True
    
    if cell1 == '#' and cell2 == '#' and cell3 == '#' and cell4 == '#':
        return True
    
    return False

def has2x2Square(input):
    for i in range(0, 4):
        for j in range(0, 4):
            if isSquare(input[i][j], input[i][j + 1], input[i + 1][j], input[i + 1][j + 1]):
                return True
            
    return False

def isRepaintable(input):
    for i in range(0, 4):
        for j in range(0, 4):
            if input[i][j] == '.':
                if isSameColor('#', input[i][j + 1], input[i + 1][j], input[i + 1][j + 1]):
                    return True
            else:
                if isSameColor('.', input[i][j + 1], input[i + 1][j], input[i + 1][j + 1]):
                    return True
            
    return False

input = []
for i in range(0, 4):
    input.append(input())
    
if has2x2Square(input):
    print('YES')
elif isRepaintable(input):
    print('YES')
else:
    print('NO')

