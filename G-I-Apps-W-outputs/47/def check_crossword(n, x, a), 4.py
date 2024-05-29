
def check_crossword(n, x, a):
    total_segments = sum(a)
    total_spaces = n - 1
    space_count = x - total_segments

    if space_count < total_spaces:
        return "NO"
    elif space_count == total_spaces:
        return "YES"
    else:
        return "NO"

# Input parsing
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Checking if there is exactly one crossword with chosen length and encoding
result = check_crossword(n, x, a)
print(result)
```
