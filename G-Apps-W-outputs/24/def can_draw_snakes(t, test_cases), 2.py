
def can_draw_snakes(t, test_cases):
    for i in range(t):
        n, m, sheet = test_cases[i]

        snakes = []
        snake_chars = {}
        current_char = 'a'

        for r in range(n):
            for c in range(m):
                if sheet[r][c] != '.':
                    if sheet[r][c] not in snake_chars:
                        snake_chars[sheet[r][c]] = [(r, c)]
                    else:
                        snake_chars[sheet[r][c]].append((r, c))

        for char in sorted(snake_chars.keys()):
            cells = snake_chars[char]
            r1, c1 = cells[0]
            r2, c2 = cells[-1]

            if r1 == r2:
                for c in range(c1, c2 + 1):
                    if sheet[r1][c] == '.':
                        sheet[r1][c] = current_char
                snakes.append((r1+1, c1+1, r2+1, c2+1))
            else:
                for r in range(r1, r2 + 1):
                    if sheet[r][c1] == '.':
                        sheet[r][c1] = current_char
                snakes.append((r1+1, c1+1, r2+1, c1+1))

            current_char = chr(ord(current_char) + 1)

        print("YES")
        print(len(snakes))
        for snake in snakes:
            print(*snake)

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    sheet = [list(input()) for _ in range(n)]
    test_cases.append((n, m, sheet))

can_draw_snakes(t, test_cases)
