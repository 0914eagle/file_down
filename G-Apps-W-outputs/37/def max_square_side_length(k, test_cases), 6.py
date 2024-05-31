
def max_square_side_length(k, test_cases):
    results = []
    for test_case in test_cases:
        n = test_case[0]
        planks = test_case[1]
        planks.sort(reverse=True)
        
        max_side_length = 0
        for i in range(n):
            side_length = min(i + 1, planks[i])
            max_side_length = max(max_side_length, side_length)
        
        results.append(max_side_length)
    
    return results

# Input parsing
k = int(input())
test_cases = []
for _ in range(k):
    n = int(input())
    planks = list(map(int, input().split()))
    test_cases.append((n, planks))

# Calculate and output results
output = max_square_side_length(k, test_cases)
for result in output:
    print(result)
