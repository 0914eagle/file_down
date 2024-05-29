
def check_crossword(n, x, encoding):
    total_length = sum(encoding) + len(encoding) - 1
    if total_length == x:
        return "YES"
    else:
        return "NO"

# Input reading
n, x = map(int, input().split())
encoding = list(map(int, input().split()))

# Check the crossword
result = check_crossword(n, x, encoding)
print(result)
```
