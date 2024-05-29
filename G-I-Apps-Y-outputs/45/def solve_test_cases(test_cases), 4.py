
def solve_test_cases(test_cases):
    results = []
    
    for n, m in test_cases:
        if n == 1:
            results.append(0)  # Only one element in array, so the result is always 0
        elif n == 2:
            results.append(m)  # For two elements, the result is the sum m
        else:
            # Construct the array where the elements alternate between 0 and m
            # This will result in the maximum sum of absolute differences
            k = m // (n // 2 + 1)
            remaining = m % (n // 2 + 1)
            result = k * (k + 1) // 2 * (n // 2) + k * remaining
            
            results.append(result)
    
    return results

# Input reading and test case processing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    test_cases.append((n, m))

results = solve_test_cases(test_cases)

# Output the results
for r in results:
    print(r)
