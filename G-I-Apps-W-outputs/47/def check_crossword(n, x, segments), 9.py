
def check_crossword(n, x, segments):
    if sum(segments) + len(segments) - 1 == x:
        return "YES"
    else:
        return "NO"

# Input parsing
n, x = map(int, input().split())
segments = list(map(int, input().split()))

# Check if there exists exactly one crossword with chosen length and encoding
result = check_crossword(n, x, segments)
print(result)
```
