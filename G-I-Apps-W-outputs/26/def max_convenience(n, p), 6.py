
def max_convenience(n, p):
    result = n*n
    cycle = [0]*n
    for i in range(n):
        cycle[i] = 1
        j = p[i]-1
        while j != i:
            cycle[i] += 1
            j = p[j]-1

    for c in cycle:
        result += c*(c-1)

    return result

# Input
n = int(input())
p = list(map(int, input().split()))

# Output
print(max_convenience(n, p))
```
