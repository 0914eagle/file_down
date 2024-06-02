
def min_cost_path(t, test_cases):
    results = []
    
    for i in range(t):
        x, y = test_cases[i][0]
        costs = test_cases[i][1]
        
        min_cost = float('inf')
        
        # Calculate the minimum cost based on the target coordinates
        if x >= 0 and y >= 0:
            min_cost = min(min_cost, x * costs[0] + y * costs[1], (x + y) * costs[2])
        elif x <= 0 and y >= 0:
            min_cost = min(min_cost, abs(x) * costs[3] + y * costs[4], (abs(x) + y) * costs[5])
        elif x >= 0 and y <= 0:
            min_cost = min(min_cost, x * costs[5] + abs(y) * costs[3], (x + abs(y)) * costs[4])
        else:
            min_cost = min(min_cost, abs(x) * costs[2] + abs(y) * costs[0], (abs(x) + abs(y)) * costs[1])
        
        results.append(min_cost)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    target = tuple(map(int, input().split()))
    costs = list(map(int, input().split()))
    test_cases.append((target, costs))

# Call the function and print the results
results = min_cost_path(t, test_cases)
for result in results:
    print(result)
