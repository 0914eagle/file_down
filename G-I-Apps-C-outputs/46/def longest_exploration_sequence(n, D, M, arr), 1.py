
def longest_exploration_sequence(n, D, M, arr):
    def explore(index, visited):
        if index < 0 or index >= n:
            return 0
        
        visited.add(index)
        max_length = 1

        for i in range(index - D, index + D + 1):
            if i in visited:
                continue
            
            if abs(arr[i] - arr[index]) <= M:
                max_length = max(max_length, 1 + explore(i, visited.copy()))
        
        visited.remove(index)
        return max_length

    max_sequence = 0
    for i in range(n):
        sequence = explore(i, set())
        max_sequence = max(max_sequence, sequence)
    
    return max_sequence

# Read input
n, D, M = map(int, input().split())
arr = list(map(int, input().split()))

# Output
print(longest_exploration_sequence(n, D, M, arr))
```
