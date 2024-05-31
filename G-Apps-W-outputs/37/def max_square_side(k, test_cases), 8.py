
def max_square_side(k, test_cases):
    res = []
    for tc in test_cases:
        n = tc[0]
        planks = tc[1]
        planks.sort(reverse=True)
        
        max_side = min(n, planks[0])
        for i in range(1, n):
            max_side = min(max_side, min(i+1, planks[i]))
        
        res.append(max_side)
    
    return res

# Input reading
k = int(input())
test_cases = []
for _ in range(k):
    n = int(input())
    planks = list(map(int, input().split()))
    test_cases.append((n, planks))

# Calculate and output results
results = max_square_side(k, test_cases)
for r in results:
    print(r)
