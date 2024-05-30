
def max_visitors(t, test_cases):
    results = []
    
    for i in range(t):
        a, b, c = test_cases[i]
        
        max_visitors = min(a, b, c)
        
        if a + b + c >= 2 * max_visitors:
            results.append(max_visitors)
        else:
            results.append((a + b + c) // 2)
    
    return results

# Input
t = int(input())
test_cases = []
for _ in range(t):
    a, b, c = map(int, input().split())
    test_cases.append((a, b, c))

# Output
results = max_visitors(t, test_cases)
for result in results:
    print(result)
```
