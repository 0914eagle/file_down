
def count_almost_palindromic_substrings(S, L, R):
    # Function to check if a string is almost palindromic
    def is_almost_palindromic(sub):
        return sub == sub[::-1] or sub[:len(sub)//2] == sub[:len(sub)//2-1:-1] or sub[1:len(sub)//2+1] == sub[:len(sub)//2:-1]
    
    count = 0
    for i in range(L-1, R):
        for j in range(i, R):
            if is_almost_palindromic(S[i:j+1]):
                count += 1
    
    return count

# Input processing
N, Q = map(int, input().split())
S = input().strip()

for _ in range(Q):
    L, R = map(int, input().split())
    result = count_almost_palindromic_substrings(S, L, R)
    print(result)
```
