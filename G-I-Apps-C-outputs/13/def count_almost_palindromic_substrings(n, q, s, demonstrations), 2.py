
def count_almost_palindromic_substrings(n, q, s, demonstrations):
    def is_almost_palindrome(substring):
        return substring == substring[::-1] or substring[:len(substring)//2] == substring[:len(substring)//2-1:-1] or substring[len(substring)//2:] == substring[:len(substring)//2-1:-1]
    
    def count_substrings(string):
        count = 0
        for i in range(len(string)):
            for j in range(i + 1, len(string) + 1):
                if is_almost_palindrome(string[i:j]):
                    count += 1
        return count

    results = []
    for demonstration in demonstrations:
        l, r = demonstration
        results.append(count_substrings(s[l-1:r]))

    return results

# Input parsing
n, q = map(int, input().split())
s = input()
demonstrations = [list(map(int, input().split())) for _ in range(q)]

# Calling the function and printing the results
results = count_almost_palindromic_substrings(n, q, s, demonstrations)
for res in results:
    print(res)
```
