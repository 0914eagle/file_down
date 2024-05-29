
def last_child(n, m, candies):
    line = list(range(1, n+1))
    index = 0
    while line:
        if candies[index] <= m:
            line.pop(index)
        else:
            line.append(line.pop(index))
        candies[index] = max(0, candies[index] - m)
        index = (index + 1) % len(line)
    
    return line[-1]

# Input parsing
n, m = map(int, input().split())
candies = list(map(int, input().split()))

# Output
print(last_child(n, m, candies))
```
