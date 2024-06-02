
def find_common_subsequence(t, test_cases):
    results = []
    
    for _ in range(t):
        n, m, a, b = test_cases[_]
        common_subsequence = []
        
        for i in range(n):
            if a[i] in b:
                common_subsequence.append(a[i])
                break
        
        if len(common_subsequence) > 0:
            results.append((True, 1, common_subsequence))
        else:
            results.append((False,))
    
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
    if result[0]:
        print("YES")
        print(result[1], end=' ')
        print(*result[2])
    else:
        print("NO")
