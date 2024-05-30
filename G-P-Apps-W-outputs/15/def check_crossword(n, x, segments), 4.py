
def check_crossword(n, x, segments):
    total_length = sum(segments) + n - 1
    if total_length == x:
        return "YES"
    else:
        return "NO"

# Input processing
n, x = map(int, input().split())
segments = list(map(int, input().split()))

# Call the function and print the result
result = check_crossword(n, x, segments)
print(result)
```
