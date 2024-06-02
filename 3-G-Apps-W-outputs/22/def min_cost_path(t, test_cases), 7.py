
def min_cost_path(t, test_cases):
    def min_cost(x, y, costs):
        if x == 0 and y == 0:
            return 0
        min_cost = float('inf')
        for dx, dy, cost in zip([1, 0, -1, -1, 0, 1], [-1, -2, -1, 1, 2, 1], costs):
            new_x, new_y = x + dx, y + dy
            new_cost = cost + min_cost(new_x, new_y, costs)
            min_cost = min(min_cost, new_cost)
        return min_cost

    results = []
    for i in range(t):
        x, y = test_cases[i][0], test_cases[i][1]
        costs = test_cases[i][2]
        results.append(min_cost(x, y, costs))
    
    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    x, y = map(int, input().split())
    costs = list(map(int, input().split()))
    test_cases.append((x, y, costs))

# Calculate and output results
results = min_cost_path(t, test_cases)
for result in results:
    print(result)
