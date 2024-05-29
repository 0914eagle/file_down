
def longest_exploration_sequence(n, D, M, array):
    def explore(index, visited):
        nonlocal max_length
        max_length = max(max_length, len(visited))
        
        for i in range(n):
            if i not in visited and abs(array[index] - array[i]) <= M and abs(index - i) <= D:
                explore(i, visited + [i])
    
    max_length = 0
    for i in range(n):
        explore(i, [i])
    
    return max_length

# Read input
n, D, M = map(int, input().split())
array = list(map(int, input().split()))

# Calculate and print the length of the longest exploration sequence
print(longest_exploration_sequence(n, D, M, array))
```
