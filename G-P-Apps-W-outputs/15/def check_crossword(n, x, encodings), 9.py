
def check_crossword(n, x, encodings):
    total_length = sum(encodings) + n - 1
    if total_length == x:
        return "YES"
    else:
        return "NO"

# Input
n, x = map(int, input().split())
encodings = list(map(int, input().split()))

# Check if there is exactly one crossword with chosen length and encoding
result = check_crossword(n, x, encodings)
print(result)
```
