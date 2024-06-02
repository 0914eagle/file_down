
def find_common_subsequence(t, test_cases):
    results = []
    
    for _ in range(t):
        n, m, a, b = test_cases[_]
        
        common_elements = set(a) & set(b)
        
        if common_elements:
            k = 1
            c = common_elements.pop()
            results.append(("YES", k, c))
        else:
            results.append(("NO",))
    
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
    print(result[0])
    if result[0] == "YES":
        print(result[1])
        print(" ".join(str(x) for x in result[2]))

