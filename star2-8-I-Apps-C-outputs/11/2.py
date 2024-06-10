

def wrap(number, maximum):
    return number % maximum

def nextColor(currentColor):
    colorList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return colorList[wrap(colorList.index(currentColor) + 1, len(colorList))]

def move(currentRow, currentColumn, direction, stepSize):
    if direction == 0:
        currentRow -= stepSize
    elif direction == 1:
        currentColumn += stepSize
    elif direction == 2:
        currentRow += stepSize
    elif direction == 3:
        currentColumn -= stepSize
    return currentRow, currentColumn

def rotate(direction):
    return (direction + 1) % 4

def cleanIce(rinkRows, rinkColumns, startRow, startColumn, numSteps):
    rink = [['.' for _ in range(rinkColumns)] for _ in range(rinkRows)]
    currentRow = startRow - 1
    currentColumn = startColumn - 1
    currentDirection = 0
    currentColor = 'A'
    for step in range(numSteps):
        currentRow, currentColumn = move(currentRow, currentColumn, currentDirection, 1)
        currentDirection = rotate(currentDirection)
        currentColor = nextColor(currentColor)
        rink[currentRow][currentColumn] = currentColor
    rink[currentRow][currentColumn] = '@'
    return rink

rinkRows, rinkColumns, startRow, startColumn, numSteps = map(int, input().split())
rink = cleanIce(rinkRows, rinkColumns, startRow, startColumn, numSteps)
for row in rink:
    print(''.join(row))

