
def solve_snakes(t, test_cases):
    def find_empty_cells(n, m, sheet):
        empty_cells = []
        for i in range(n):
            for j in range(m):
                if sheet[i][j] == '.':
                    empty_cells.append((i, j))
        return empty_cells

    def draw_snakes(n, m, sheet):
        snakes = []
        empty_cells = find_empty_cells(n, m, sheet)

        def draw_snake(r1, c1, r2, c2):
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    sheet[i][j] = chr(ord('a') + len(snakes))

        while empty_cells:
            r1, c1 = empty_cells.pop()
            r2, c2 = r1, c1
            while r2 + 1 < n and sheet[r2 + 1][c1] == '.':
                r2 += 1
            while c2 + 1 < m and sheet[r1][c2 + 1] == '.':
                c2 += 1
            draw_snake(r1, c1, r2, c2)
            snakes.append((r1 + 1, c1 + 1, r2 + 1, c2 + 1))

        return snakes

    results = []
    for i in range(t):
        n, m = test_cases[i][0], test_cases[i][1]
        sheet = test_cases[i][2:]
        snakes = draw_snakes(n, m, sheet)

        if len(snakes) <= 26:
            results.append("YES")
            results.append(str(len(snakes)))
            for snake in snakes:
                results.append(" ".join(map(str, snake)))
        else:
            results.append("NO")

    return results


# Input
t = 2
test_cases = [
    (3, 3, ['...', '.a.', '...']),
    (2, 2, ['bb', 'cc'])
]

# Solve and print output
output = solve_snakes(t, test_cases)
for line in output:
    print(line)
