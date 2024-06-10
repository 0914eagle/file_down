
import sys

def solve(data):
    for i in range(4):
        for j in range(4):
            if (data[i][j] == '#'):
                data[i][j] = '.'
            else:
                data[i][j] = '#'

            if (check(data)):
                return 'YES'

            if (data[i][j] == '#'):
                data[i][j] = '.'
            else:
                data[i][j] = '#'
    
    return 'NO'


def check(data):
    for i in range(3):
        for j in range(3):
            if (data[i][j] == data[i][j + 1] == data[i + 1][j] == data[i + 1][j + 1]):
                return True
    
    return False


data = []
for _ in range(4):
    data.append(list(sys.stdin.readline().strip()))

print(solve(data))

