
def last_child(n, m, candies_required):
    children = list(range(1, n+1))
    index = 0

    while len(children) > 0:
        if candies_required[index] <= m:
            children.pop(index)
        else:
            candies_required[index] -= m
            children.append(children.pop(index))

    return children[-1]

# Input processing
n, m = map(int, input().split())
candies_required = list(map(int, input().split()))

result = last_child(n, m, candies_required)
print(result)
```
