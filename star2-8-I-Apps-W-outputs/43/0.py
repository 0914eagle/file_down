
board = [list(input()) for _ in range(8)]
for i in range(8):
    for j in range(8):
        if board[i][j] == 'T':
            start_row, start_col = i, j
def is_program_valid(program):
    row, col = start_row, start_col
    direction = 0  # 0: right, 1: down, 2: left, 3: up
    for instruction in program:
        if instruction == 'F':
            if direction == 0:
                col += 1
            elif direction == 1:
                row += 1
            elif direction == 2:
                col -= 1
            else:
                row -= 1
            if row < 0 or row >= 8 or col < 0 or col >= 8 or board[row][col] in ('C', 'I'):
                return False
        elif instruction == 'R':
            direction = (direction + 1) % 4
        elif instruction == 'L':
            direction = (direction - 1) % 4
        elif instruction == 'X':
            if direction == 0:
                col += 1
            elif direction == 1:
                row += 1
            elif direction == 2:
                col -= 1
            else:
                row -= 1
            if row < 0 or row >= 8 or col < 0 or col >= 8 or board[row][col] != 'I':
                return False
            board[row][col] = '.'
        else:
            return False
    return board[row][col] == 'D'

def find_shortest_program():
    queue = ['']
    shortest_program = None
    while queue:
        program = queue.pop(0)
        if is_program_valid(program):
            if shortest_program is None or len(program) < len(shortest_program):
                shortest_program = program
            if shortest_program is not None and len(program) == len(shortest_program):
                return shortest_program
            queue.append(program + 'F')
            queue.append(program + 'R')
            queue.append(program + 'L')
            queue.append(program + 'X')
    return 'no solution'

print(find_shortest_program())

