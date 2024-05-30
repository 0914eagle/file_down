
def find_crashing_line_time(n, r, p):
    if n == 1:
        return 0
    low = 0
    high = r
    while low < high:
        mid = (low + high) // 2
        if (mid // p) * n >= mid:
            high = mid
        else:
            low = mid + 1
    return high

# Read input
n, r, p = map(int, input().split())

# Call the function and output the result
print(find_crashing_line_time(n, r, p))
```
