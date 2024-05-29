
def longest_exploration(n, D, M, array):
    def explore(curr_index, visited):
        max_length = 0
        visited.add(curr_index)
        for i in range(n):
            if i not in visited and abs(array[i] - array[curr_index]) <= M and abs(i - curr_index) <= D:
                max_length = max(max_length, 1 + explore(i, visited.copy()))
        visited.remove(curr_index)
        return max_length

    max_length = 0
    for i in range(n):
        max_length = max(max_length, explore(i, set()))

    return max_length

# Read input
n, D, M = map(int, input().split())
array = list(map(int, input().split()))

# Calculate and print the result
result = longest_exploration(n, D, M, array)
print(result)
```
