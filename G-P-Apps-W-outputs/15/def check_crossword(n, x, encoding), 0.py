
def check_crossword(n, x, encoding):
    total_segments = sum(encoding)
    total_length = total_segments + len(encoding) - 1
    if total_length == x and total_segments == x:
        return "YES"
    return "NO"

# Input parsing
n, x = map(int, input().split())
encoding = list(map(int, input().split()))

# Check if one crossword with given length and encoding exists
result = check_crossword(n, x, encoding)
print(result)
```
