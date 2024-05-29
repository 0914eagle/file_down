
def explore_array(n, D, M, array):
    def dfs(idx, visited):
        nonlocal max_length
        visited.add(idx)
        max_length = max(max_length, len(visited))
        for i in range(n):
            if i not in visited and abs(array[i] - array[idx]) <= M and abs(i - idx) <= D:
                dfs(i, visited.copy())
    
    max_length = 0
    for i in range(n):
        visited = set()
        dfs(i, visited)
    
    return max_length

# Reading input
n, D, M = map(int, input().split())
array = list(map(int, input().split()))

# Calling the function
result = explore_array(n, D, M, array)

# Output
print(result)
```
