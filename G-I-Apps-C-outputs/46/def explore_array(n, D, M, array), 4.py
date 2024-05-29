
def explore_array(n, D, M, array):
    def dfs(index, visited):
        max_length = 0
        for i in range(n):
            if i not in visited and abs(array[i] - array[index]) <= M and abs(i - index) <= D:
                new_visited = set(visited)
                new_visited.add(i)
                max_length = max(max_length, 1 + dfs(i, new_visited))
        return max_length

    max_sequence_length = 0
    for i in range(n):
        max_sequence_length = max(max_sequence_length, dfs(i, {i}))
    
    return max_sequence_length

# Read input
n, D, M = map(int, input().split())
array = list(map(int, input().split()))

# Get the length of the longest exploration sequence
result = explore_array(n, D, M, array)
print(result)
```
