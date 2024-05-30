
def is_valid_crossword(n, x, encoding):
    total_length = sum(encoding)
    num_segments = len(encoding)
    
    if total_length + num_segments - 1 > x:
        return "NO"
    elif total_length + num_segments - 1 < x:
        return "NO"
    elif total_length < x:
        return "NO"
    else:
        return "YES"

# Input
n, x = map(int, input().split())
encoding = list(map(int, input().split()))

# Check if there exists exactly one valid crossword
result = is_valid_crossword(n, x, encoding)
print(result)
```
