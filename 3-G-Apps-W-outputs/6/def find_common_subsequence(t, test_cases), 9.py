
def find_common_subsequence(t, test_cases):
    results = []
    
    for _ in range(t):
        n, m, a, b = test_cases[_]
        
        common_elements = set(a) & set(b)
        
        if len(common_elements) > 0:
            results.append("YES")
            results.append("1 " + str(list(common_elements)[0]))
        else:
            results.append("NO")
    
    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, m, a, b))

# Find common subsequences
results = find_common_subsequence(t, test_cases)

# Output results
for result in results:
    print(result)
