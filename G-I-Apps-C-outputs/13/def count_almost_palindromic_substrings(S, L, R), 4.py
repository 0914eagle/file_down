
def count_almost_palindromic_substrings(S, L, R):
    def is_almost_palindrome(sub):
        return sub == sub[::-1] or len(set(sub)) == len(sub) - 2

    count = 0
    for i in range(L-1, R):
        for j in range(i, R):
            if is_almost_palindrome(S[i:j+1]):
                count += 1
    return count

# Input parsing
N, Q = map(int, input().split())
S = input()

for _ in range(Q):
    L, R = map(int, input().split())
    result = count_almost_palindromic_substrings(S, L, R)
    print(result)
```
