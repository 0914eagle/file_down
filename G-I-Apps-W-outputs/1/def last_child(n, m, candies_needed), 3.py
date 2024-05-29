
def last_child(n, m, candies_needed):
    candies_left = [m] * n
    queue = list(range(n))

    while queue:
        child = queue.pop(0)
        if candies_left[child] <= candies_needed[child]:
            candies_left[child] = 0
            continue
        candies_left[child] -= candies_needed[child]
        queue.append(child)

    return child + 1

# Input
n, m = map(int, input().split())
candies_needed = list(map(int, input().split()))

# Output
print(last_child(n, m, candies_needed))
```
