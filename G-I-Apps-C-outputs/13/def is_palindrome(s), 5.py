
def is_palindrome(s):
    return s == s[::-1]

def count_almost_palindromic_substrings(s, l, r):
    count = 0
    for i in range(l-1, r):
        for j in range(i, r):
            if is_palindrome(s[i:j+1]) or is_palindrome(s[i:j+1][::-1]):
                count += 1
    return count

def count_almost_palindromic_substrings_demonstrations(N, Q, S, demonstrations):
    result = []
    for l, r in demonstrations:
        result.append(count_almost_palindromic_substrings(S, l, r))
    return result

# Input
N, Q = map(int, input().split())
S = input().strip()
demonstrations = [list(map(int, input().split())) for _ in range(Q)]

# Output
output = count_almost_palindromic_substrings_demonstrations(N, Q, S, demonstrations)
for val in output:
    print(val)
```
