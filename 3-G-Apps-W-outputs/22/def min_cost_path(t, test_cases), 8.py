
def min_cost_path(t, test_cases):
    for i in range(t):
        x, y = test_cases[i][0]
        c = test_cases[i][1]

        if x == 0 and y == 0:
            print(0)
        else:
            if x * y > 0:
                print(min(abs(x) * c[0] + abs(y) * c[1], (abs(x) + abs(y)) * c[2]))
            else:
                print((abs(x) + abs(y)) * c[3])

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    x, y = map(int, input().split())
    costs = list(map(int, input().split()))
    test_cases.append(((x, y), costs))

min_cost_path(t, test_cases)
