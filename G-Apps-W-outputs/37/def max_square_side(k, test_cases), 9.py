
def max_square_side(k, test_cases):
    results = []
    
    for i in range(k):
        n = test_cases[i][0]
        planks = test_cases[i][1]
        
        max_side = min(max(planks), n)
        results.append(max_side)
    
    return results

# Input parsing
k = int(input())
test_cases = []
for _ in range(k):
    n = int(input())
    planks = list(map(int, input().split()))
    test_cases.append((n, planks))

# Call the function and output the results
results = max_square_side(k, test_cases)
for result in results:
    print(result)
