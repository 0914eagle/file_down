
def find_common_subsequence(t, test_cases):
    results = []
    
    for i in range(t):
        n, m = test_cases[i][0]
        a = test_cases[i][1]
        b = test_cases[i][2]
        
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

# Call the function and output the results
results = find_common_subsequence(t, test_cases)
for res in results:
    print(res)
