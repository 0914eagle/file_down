
def max_square_length(k, test_cases):
    results = []
    
    for case in test_cases:
        n = case[0]
        planks = case[1]
        
        planks.sort(reverse=True)
        
        side_length = min(n, max([min(i+1, plank) for i, plank in enumerate(planks)]))
        
        results.append(side_length)
    
    return results

# Input
k = int(input())
test_cases = []
for _ in range(k):
    n = int(input())
    planks = list(map(int, input().split()))
    test_cases.append((n, planks))

# Output
output = max_square_length(k, test_cases)
for result in output:
    print(result)
