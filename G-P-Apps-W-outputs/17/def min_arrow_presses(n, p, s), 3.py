
def min_arrow_presses(n, p, s):
    p -= 1  # Convert 1-based indexing to 0-based indexing
    total_presses = 0
    for i in range(n // 2):
        diff = abs(ord(s[i]) - ord(s[n - 1 - i]))
        total_presses += min(diff, 26 - diff)
    
    cursor_to_middle = min(abs(p - n//2), abs(p - n//2 - 1))  # Move cursor to the middle of the string
    return total_presses + cursor_to_middle

# Input processing
n, p = map(int, input().split())
string = input().strip()

# Call the function and print the result
print(min_arrow_presses(n, p, string))
```
