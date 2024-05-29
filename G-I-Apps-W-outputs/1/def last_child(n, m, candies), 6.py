
def last_child(n, m, candies):
    remaining_candies = list(candies)
    line = list(range(1, n+1))
    
    while len(line) > 0:
        child = line.pop(0)
        if remaining_candies[child-1] <= m:
            continue
        
        remaining_candies[child-1] -= m
        line.append(child)
    
    return child

# Input parsing
n, m = map(int, input().split())
candies = list(map(int, input().split()))

# Output
print(last_child(n, m, candies))
```
