
def max_absolute_diff(t, test_cases):
    result = []
    
    for tc in test_cases:
        n, m = tc
        if n == 1:
            result.append(0)
        elif n == 2:
            result.append(min(2, m))
        else:
            result.append(2 * m)
    
    return result

# Input processing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    test_cases.append((n, m))

# Calculate and output results
results = max_absolute_diff(t, test_cases)
for res in results:
    print(res)
