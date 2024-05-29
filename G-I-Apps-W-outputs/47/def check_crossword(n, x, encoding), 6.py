
def check_crossword(n, x, encoding):
    total_length = sum(encoding) + n - 1
    if total_length == x:
        return "YES"
    else:
        return "NO"
    
# Input
n, x = map(int, input().split())
encoding = list(map(int, input().split()))

# Check crossword
result = check_crossword(n, x, encoding)
print(result)
```
