
def find_crashing_line_time(n, r, p):
    if n == 1:
        return 0
    low, high = 0, r
    while low < high:
        mid = (low + high) // 2
        if mid * (n - 1) + p * (n - 1) <= r - mid:
            low = mid + 1
        else:
            high = mid
    return low - 1

# Read input
n, r, p = map(int, input().split())
# Call the function and output the result
print(find_crashing_line_time(n, r, p))
```
