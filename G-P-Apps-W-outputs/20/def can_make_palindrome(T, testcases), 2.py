
def can_make_palindrome(T, testcases):
    def is_palindrome(s):
        return s == s[::-1]
    
    results = []
    for _ in range(T):
        n = testcases.pop(0)
        s = testcases.pop(0)
        
        changes_possible = True
        for i in range(n // 2):
            diff = abs(ord(s[i]) - ord(s[n-i-1]))
            if diff != 0 and diff != 2:
                changes_possible = False
                break
        
        if changes_possible and is_palindrome(s):
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Input parsing
T = int(input())
testcases = []
for _ in range(T):
    n = int(input())
    s = input().strip()
    testcases.extend([n, s])

# Solve the problem for the given testcases
results = can_make_palindrome(T, testcases)

# Output the results
for res in results:
    print(res)
