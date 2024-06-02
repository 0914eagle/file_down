
def find_common_subsequence(t, test_cases):
    results = []
    
    for i in range(t):
        n, m, a, b = test_cases[i]
        common_subsequence = []
        
        for num in a:
            if num in b:
                common_subsequence.append(num)
        
        if len(common_subsequence) > 0:
            results.append("YES")
            results.append(str(len(common_subsequence)))
            results.append(" ".join(map(str, common_subsequence)))
        else:
            results.append("NO")
    
    return results

# Input processing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, m, a, b))

# Call the function and output the results
output = find_common_subsequence(t, test_cases)
for line in output:
    print(line)
