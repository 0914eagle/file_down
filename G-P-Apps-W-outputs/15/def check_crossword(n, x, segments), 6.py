
def check_crossword(n, x, segments):
    total_length = sum(segments) + n - 1
    if total_length == x:
        return "YES"
    else:
        return "NO"

# Input parsing
n, x = map(int, input().split())
segments = list(map(int, input().split()))

result = check_crossword(n, x, segments)
print(result)
```
