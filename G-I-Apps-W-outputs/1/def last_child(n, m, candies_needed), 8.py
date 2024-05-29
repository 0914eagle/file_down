
def last_child(n, m, candies_needed):
    children = list(range(1, n+1))
    idx = 0
    while len(children) > 1:
        if candies_needed[idx] <= m:
            children.pop(idx)
        else:
            children.append(children.pop(idx))
        candies_needed[idx] = max(0, candies_needed[idx] - m)
        idx = (idx + 1) % len(children)
    return children[0]

# Input
n, m = map(int, input().split())
candies_needed = list(map(int, input().split()))

# Output
print(last_child(n, m, candies_needed))
```
