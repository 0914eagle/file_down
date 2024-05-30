
def check_crossword(n, x, encoding):
    total_length = sum(encoding) + len(encoding) - 1
    if total_length > x:
        return "NO"
    if total_length == x:
        return "YES"
    return "NO"

# Input
n, x = map(int, input().split())
encoding = list(map(int, input().split()))

# Output
print(check_crossword(n, x, encoding))
```
