
def check_crossword(n, x, a):
    total_length = sum(a) + n - 1
    if total_length == x:
        return "YES"
    else:
        return "NO"

# Input processing
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Check if there exists exactly one crossword with chosen length and encoding
result = check_crossword(n, x, a)
print(result)
```
