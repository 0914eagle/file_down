
def convenience_count(n, p):
    result = n  # Counting (x, x) pairs
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            cycle_nodes = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = p[j] - 1
                cycle_nodes += 1

            result += cycle_nodes * (cycle_nodes - 1)

    return result

# Taking input from the user
n = int(input())
p = list(map(int, input().split()))

# Calculating and printing the maximum possible convenience
print(convenience_count(n, p))
```
