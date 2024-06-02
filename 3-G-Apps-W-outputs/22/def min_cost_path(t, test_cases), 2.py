
def min_cost_path(t, test_cases):
    results = []
    
    for i in range(t):
        x, y = test_cases[i][0]
        c = test_cases[i][1]
        
        min_cost = abs(x) * min(c[0], c[2], c[4]) + abs(y) * min(c[1], c[3], c[5])
        
        if x * y >= 0:
            min_cost += abs(x + y) * min(c[0], c[1], c[5])
        else:
            min_cost += max(abs(x), abs(y)) * min(c[2], c[3], c[4])
        
        results.append(min_cost)
    
    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    x, y = map(int, input().split())
    c = list(map(int, input().split()))
    test_cases.append(((x, y), c))

# Calculate and output results
results = min_cost_path(t, test_cases)
for res in results:
    print(res)
