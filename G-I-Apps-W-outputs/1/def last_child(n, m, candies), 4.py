
def last_child(n, m, candies):
    line = list(range(1, n+1))
    
    while line:
        child = line.pop(0)
        if candies[child-1] <= m:
            continue
        else:
            candies[child-1] -= m
            line.append(child)
    
    return child

# Input
n, m = map(int, input().split())
candies = list(map(int, input().split()))

# Output
print(last_child(n, m, candies))
```
