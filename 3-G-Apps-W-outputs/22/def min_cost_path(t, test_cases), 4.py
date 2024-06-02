
def min_cost_path(t, test_cases):
    def hexagonal_distance(x, y):
        return max(abs(x), abs(y), abs(x + y))

    results = []
    for i in range(t):
        x, y = test_cases[i][0], test_cases[i][1]
        c = test_cases[i][2]

        dist = hexagonal_distance(x, y)
        if dist == 0:
            results.append(0)
        else:
            results.append(min(c) * dist + min(c[min(0, x, y):max(0, x, y)])

    return results


# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    x, y = map(int, input().split())
    c = list(map(int, input().split()))
    test_cases.append((x, y, c))

# Call the function and print the results
results = min_cost_path(t, test_cases)
for res in results:
    print(res)
