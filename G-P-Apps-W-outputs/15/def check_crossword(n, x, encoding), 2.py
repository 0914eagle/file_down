
def check_crossword(n, x, encoding):
    total_segments = sum(encoding)
    total_length = x + n - 1
    if total_segments != n or total_length > x:
        return "NO"
    return "YES"

# Input
n, x = map(int, input().split())
encoding = list(map(int, input().split()))

# Check crossword
result = check_crossword(n, x, encoding)
print(result)
```
