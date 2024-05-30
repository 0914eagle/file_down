
def find_crashing_line(n, r, p):
    def binary_search(l, r, n, p):
        if l == r:
            return l * p
        mid = (l + r) // 2
        if mid * p + (n - mid) * p < r:
            return binary_search(mid + 1, r, n, p)
        else:
            return binary_search(l, mid, n, p)

    return binary_search(0, n, n, p)

# Read input
n, r, p = map(int, input().split())

# Find the worst-case time to find the crashing line
result = find_crashing_line(n, r, p)

# Output the result
print(result)
```
