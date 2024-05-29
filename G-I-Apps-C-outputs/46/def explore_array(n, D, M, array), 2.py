
def explore_array(n, D, M, array):
    max_length = 0
    
    def explore(index, visited):
        nonlocal max_length
        max_length = max(max_length, len(visited))
        
        for i in range(index+1, min(index+D+1, n)):
            if abs(array[i] - array[index]) <= M and i not in visited:
                explore(i, visited + [i])
    
    for i in range(n):
        explore(i, [i])
    
    return max_length

# Read input
n, D, M = map(int, input().split())
array = list(map(int, input().split()))

# Print output
print(explore_array(n, D, M, array))
```
