
def checkered_snakes(t, test_cases):
    def find_snakes(n, m, sheet):
        snakes = []
        snake_count = 0
        current_snake = 'a'
        for i in range(n):
            for j in range(m):
                if sheet[i][j] == current_snake:
                    continue
                elif sheet[i][j] == '.':
                    continue
                else:
                    snake_count += 1
                    current_snake = sheet[i][j]
                    start_row = i
                    start_col = j
                    end_row = i
                    end_col = j
                    # check horizontal snake
                    for k in range(j + 1, m):
                        if sheet[i][k] == current_snake:
                            end_col = k
                        else:
                            break
                    # check vertical snake
                    for k in range(i + 1, n):
                        if sheet[k][j] == current_snake:
                            end_row = k
                        else:
                            break
                    snakes.append((start_row + 1, start_col + 1, end_row + 1, end_col + 1))
        return snake_count, snakes

    results = []
    for i in range(t):
        n, m = test_cases[i][0], test_cases[i][1]
        sheet = test_cases[i][2:]
        
        snake_count, snakes = find_snakes(n, m, sheet)

        if snake_count == 0:
            results.append(['YES', 0, []])
        else:
            results.append(['YES', snake_count, snakes])

    for res in results:
        print(res[0])
        if res[0] == 'YES':
            print(res[1])
            for snake in res[2]:
                print(' '.join(map(str, snake)))

# Example usage:
t = 3
test_cases = [
    (3, 3, ['...', '.a.', '...']),
    (4, 4, ['..c.', 'adda', 'bbcb', '....']),
    (2, 2, ['bb', 'cc'])
]

checkered_snakes(t, test_cases)
