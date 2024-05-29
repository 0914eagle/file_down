
def verify_crossword(n, x, encoding):
    total_length = sum(encoding) + len(encoding) - 1
    if total_length == x:
        return "YES"
    else:
        return "NO"

# Input parsing
n, x = map(int, input().split())
encoding = list(map(int, input().split()))

# Call the function with input values
result = verify_crossword(n, x, encoding)
print(result)
```
