
def max_square_side_length(k, test_cases):
    results = []
    for i in range(k):
        n, planks = test_cases[i]
        planks.sort(reverse=True)
        max_side_length = min(n, planks[n-1])
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
results = max_square_side_length(k, test_cases)
for result in results:
    print(result)
