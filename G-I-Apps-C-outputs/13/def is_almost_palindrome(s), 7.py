
def is_almost_palindrome(s):
    return s == s[::-1] or s[:len(s)//2] == s[:len(s)//2-1:-1] or s[:len(s)//2+1] == s[:len(s)//2:-1]

def count_almost_palindromic_substrings(s):
    count = 0
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            if is_almost_palindrome(s[i:j]):
                count += 1
    return count

def almost_palindrome_demo(N, Q, S, demonstrations):
    results = []
    for demo in demonstrations:
        L, R = demo
        substring = S[L-1:R]
        results.append(count_almost_palindromic_substrings(substring))
    return results

# Input parsing
N, Q = map(int, input().split())
S = input().strip()
demonstrations = []
for _ in range(Q):
    L, R = map(int, input().split())
    demonstrations.append((L, R))

# Solve the problem
output = almost_palindrome_demo(N, Q, S, demonstrations)

# Output the results
for result in output:
    print(result)
```

