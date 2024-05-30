
def find_crashing_line(n, r, p):
    def binary_search(left, right):
        if left == right:
            return left
        mid = (left + right) // 2
        time_to_run = p * mid
        if time_to_run >= r:
            return binary_search(left, mid)
        else:
            return binary_search(mid + 1, right)
    
    return binary_search(0, n) * p

# Input
n, r, p = map(int, input().split())

# Output
print(find_crashing_line(n, r, p))
```
