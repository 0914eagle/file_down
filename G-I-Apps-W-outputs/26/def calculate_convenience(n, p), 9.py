
def calculate_convenience(n, p):
    result = 0
    for i in range(n):
        x = i+1
        y = p.index(i+1)+1
        result += n + 2*x*y - x - y
    return result

n = int(input())
p = list(map(int, input().split()))

result = calculate_convenience(n, p)
print(result)
```
