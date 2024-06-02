
def min_cost_path(t, test_cases):
    results = []
    
    for i in range(t):
        x, y = test_cases[i][0]
        costs = test_cases[i][1]
        
        min_cost = min(abs(x) * costs[0] + abs(y) * costs[1],
                       (abs(x) + abs(y)) * costs[2],
                       abs(y) * costs[3] + abs(x) * costs[4],
                       abs(x) * costs[5] + abs(x + y) * costs[0],
                       abs(y) * costs[1] + abs(x + y) * costs[3])
        
        results.append(min_cost)
    
    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    x, y = map(int, input().split())
    costs = list(map(int, input().split()))
    test_cases.append(((x, y), costs))

# Calculate and output results
results = min_cost_path(t, test_cases)
for result in results:
    print(result)
