
def max_square_length(k, test_cases):
    results = []
    
    for _ in range(k):
        n = test_cases[_][0]
        planks = test_cases[_][1]
        
        max_length = min(max(planks), n)
        
        results.append(max_length)
    
    return results

# Input parsing
k = int(input())
test_cases = []
for _ in range(k):
    n = int(input())
    planks = list(map(int, input().split()))
    test_cases.append((n, planks))

# Call the function and print the results
results = max_square_length(k, test_cases)
for res in results:
    print(res)
