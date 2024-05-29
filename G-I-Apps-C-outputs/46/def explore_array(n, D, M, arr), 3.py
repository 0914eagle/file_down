
def explore_array(n, D, M, arr):
    def dfs(i, visited):
        nonlocal max_length
        visited.add(i)
        max_length = max(max_length, len(visited))
        for j in range(n):
            if j not in visited and abs(arr[i] - arr[j]) <= M and abs(i - j) <= D:
                dfs(j, visited.copy())
    
    max_length = 0
    for i in range(n):
        dfs(i, set())
    
    return max_length

# Read input
n, D, M = map(int, input().split())
arr = list(map(int, input().split()))

# Call the function and print the result
result = explore_array(n, D, M, arr)
print(result)
```
