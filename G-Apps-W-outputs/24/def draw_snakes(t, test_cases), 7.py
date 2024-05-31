
def draw_snakes(t, test_cases):
    def find_empty_cell(board):
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    return (i, j)
        return None

    def check_empty(board):
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    return True
        return False

    def check_neighbors(i, j, board):
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < n and 0 <= nj < m:
                if board[ni][nj] == board[i][j]:
                    return True
        return False

    def draw_snake(board, snake_char):
        result = []
        for i in range(n):
            for j in range(m):
                if board[i][j] == snake_char:
                    snake_len = 1
                    ni, nj = i, j
                    while ni+1 < n and board[ni+1][j] == snake_char:
                        snake_len += 1
                        ni += 1
                    nk, nl = i, j
                    while nl+1 < m and board[i][nl+1] == snake_char:
                        snake_len += 1
                        nl += 1
                    result.append((i+1, j+1, ni+1, nl+1))
                    for x in range(i, ni+1):
                        for y in range(j, nl+1):
                            board[x][y] = '.'
        return result

    for i in range(t):
        n, m = test_cases[i][0], test_cases[i][1]
        board = [list(input()) for _ in range(n)]

        snakes = []
        snake_char = 'a'
        while check_empty(board):
            empty_cell = find_empty_cell(board)
            if empty_cell is None:
                break
            i, j = empty_cell
            if check_neighbors(i, j, board):
                print("NO")
                break
            board[i][j] = snake_char
            snakes += draw_snake(board, snake_char)
            snake_char = chr(ord(snake_char) + 1)

        if check_empty(board):
            continue

        print("YES")
        print(len(snakes))
        for s in snakes:
            print(*s)

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    test_cases.append((n, m))

draw_snakes(t, test_cases)
