
def is_palindrome_possible(n, s):
    for i in range(n//2):
        if abs(ord(s[i]) - ord(s[n-1-i])) > 2 or abs(ord(s[i]) - ord(s[n-1-i])) == 1:
            return "NO"
    return "YES"

# Input
testcases = int(input())
for _ in range(testcases):
    n = int(input())
    s = input().strip()
    
    # Check if palindrome is possible
    result = is_palindrome_possible(n, s)
    print(result)
```
