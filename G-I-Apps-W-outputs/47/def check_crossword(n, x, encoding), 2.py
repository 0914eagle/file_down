
def check_crossword(n, x, encoding):
    total_length = sum(encoding) + n - 1
    if total_length == x:
        return "YES"
    else:
        return "NO"

# Input parsing
n, x = map(int, input().split())
encoding = list(map(int, input().split()))

# Check if there exists exactly one crossword with chosen length and encoding
result = check_crossword(n, x, encoding)
print(result)
```
