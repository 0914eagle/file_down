
def min_cost_path(t, test_cases):
    results = []
    
    for i in range(t):
        x, y = test_cases[i][0]
        c = test_cases[i][1]
        
        min_cost = 0
        if x > 0 and y > 0:
            min_cost = min(c[0] * x + c[1] * y, c[2] * (x + y))
        elif x < 0 and y < 0:
            min_cost = min(c[3] * abs(x) + c[4] * abs(y), c[5] * (abs(x) + abs(y)))
        elif x > 0 and y < 0:
            min_cost = min(c[0] * x + c[5] * abs(y), c[1] * y + c[4] * abs(x), c[2] * (x - y))
        elif x < 0 and y > 0:
            min_cost = min(c[3] * abs(x) + c[2] * y, c[4] * abs(x) + c[1] * y, c[5] * (abs(x) - y))
        else:
            min_cost = 0
        
        results.append(min_cost)
    
    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    xy = tuple(map(int, input().split()))
    costs = list(map(int, input().split()))
    test_cases.append((xy, costs))

# Calculate and output results
results = min_cost_path(t, test_cases)
for result in results:
    print(result)
