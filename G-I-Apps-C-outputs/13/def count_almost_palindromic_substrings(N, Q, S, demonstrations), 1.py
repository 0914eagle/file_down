
def count_almost_palindromic_substrings(N, Q, S, demonstrations):
    def is_almost_palindrome(substring):
        return substring == substring[::-1] or substring[:len(substring) // 2] == substring[-1:-len(substring) // 2 - 1:-1]
    
    def count_almost_palindromic_substrings_in_range(L, R):
        count = 0
        for i in range(L-1, R):
            for j in range(i, R):
                if is_almost_palindrome(S[i:j+1]):
                    count += 1
        return count
    
    result = []
    for L, R in demonstrations:
        result.append(count_almost_palindromic_substrings_in_range(L, R))
    
    return result

# Input parsing
N, Q = map(int, input().split())
S = input().strip()
demonstrations = [tuple(map(int, input().split())) for _ in range(Q)]

# Call the function and print the output
output = count_almost_palindromic_substrings(N, Q, S, demonstrations)
for count in output:
    print(count)
```
