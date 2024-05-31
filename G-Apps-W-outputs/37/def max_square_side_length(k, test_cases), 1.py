
def max_square_side_length(k, test_cases):
    results = []
    
    for i in range(k):
        n = test_cases[i][0]
        planks = test_cases[i][1]
        
        planks.sort(reverse=True)
        
        max_side_length = min(n, planks[0])
        for j in range(1, n):
            max_side_length = min(max_side_length, min(j+1, planks[j]))
        
        results.append(max_side_length)
    
    return results

# Read input
k = int(input())
test_cases = []
for _ in range(k):
    n = int(input())
    planks = list(map(int, input().split()))
    test_cases.append((n, planks))

# Get results
results = max_square_side_length(k, test_cases)

# Output results
for result in results:
    print(result)
