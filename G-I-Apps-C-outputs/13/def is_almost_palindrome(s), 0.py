
def is_almost_palindrome(s):
    return s == s[::-1] or s[:len(s)//2] == s[-1:-len(s)//2-1:-1]

def count_almost_palindromic_substrings(s, l, r):
    count = 0

    for i in range(l-1, r):
        for j in range(i, r):
            substring = s[i:j+1]
            if is_almost_palindrome(substring):
                count += 1

    return count

# Input reading
n, q = map(int, input().split())
string = input().strip()

demonstrations = []
for _ in range(q):
    l, r = map(int, input().split())
    demonstrations.append((l, r))

# Process each demonstration
for l, r in demonstrations:
    result = count_almost_palindromic_substrings(string, l, r)
    print(result)
```
