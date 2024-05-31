
def solve_snakes(t, test_cases):
    for test_case in test_cases:
        n, m = test_case[0]
        sheet = test_case[1:]

        snakes = {}
        snake_count = 0

        for i in range(n):
            for j in range(m):
                if sheet[i][j] != '.':
                    if sheet[i][j] in snakes:
                        snakes[sheet[i][j]].append((i, j))
                    else:
                        snakes[sheet[i][j]] = [(i, j)]
        
        result = []
        for key in sorted(snakes.keys()):
            snake_count += 1
            coords = snakes[key]
            r1, c1 = coords[0]
            r2, c2 = coords[-1]
            result.append((r1+1, c1+1, r2+1, c2+1))
        
        if len(result) == 0:
            print("YES")
            print("0")
        else:
            print("YES")
            print(len(result))
            for r1, c1, r2, c2 in result:
                print(r1, c1, r2, c2)


t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    sheet = []
    for _ in range(n):
        row = input()
        sheet.append(row)
    
    test_cases.append((n, m, sheet))

solve_snakes(t, test_cases)
