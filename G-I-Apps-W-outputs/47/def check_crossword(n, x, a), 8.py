
def check_crossword(n, x, a):
    total_length = sum(a) + len(a) - 1
    if total_length == x:
        return "YES"
    else:
        return "NO"

# Input parsing
n, x = map(int, input().split())
a = list(map(int, input().split()))

result = check_crossword(n, x, a)
print(result)
```
