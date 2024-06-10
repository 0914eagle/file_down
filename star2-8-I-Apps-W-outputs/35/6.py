
from itertools import product

def check_square(arr):
    for row in range(2):
        for col in range(2):
            if all(arr[row][col] == c for c in product((0, 1), repeat=4)):
                return True
    return False

def change_cell(arr):
    for row in range(4):
        for col in range(4):
            arr[row][col] = 1 - arr[row][col]
            if check_square(arr):
                return True
            arr[row][col] = 1 - arr[row][col]
    return False

def main():
    arr = [[0 if c == '.' else 1 for c in input()] for _ in range(4)]
    if check_square(arr) or change_cell(arr):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()

