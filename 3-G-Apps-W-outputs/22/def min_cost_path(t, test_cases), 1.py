
import math

def min_cost_path(t, test_cases):
    results = []
    
    for i in range(t):
        x, y, c = test_cases[i]
        
        min_cost = 0
        if x * y > 0:
            min_cost = min(abs(x), abs(y)) * c[1]
            remaining = abs(x) - min(abs(x), abs(y))
            if remaining > 0:
                min_cost += remaining * c[2]
        else:
            min_cost = (abs(x) + abs(y)) * c[3]
        
        results.append(min_cost)
    
    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    x, y = map(int, input().split())
    costs = list(map(int, input().split()))
    test_cases.append((x, y, costs))

# Call the function and print the results
results = min_cost_path(t, test_cases)
for result in results:
    print(result)
