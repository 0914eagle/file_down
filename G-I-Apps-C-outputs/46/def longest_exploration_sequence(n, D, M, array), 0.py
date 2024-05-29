
def longest_exploration_sequence(n, D, M, array):
    def helper(start, visited):
        max_length = 0
        for i in range(start, n):
            if i in visited:
                continue
            if not visited or abs(array[i] - array[visited[-1]]) <= M:
                new_visited = visited + [i]
                max_length = max(max_length, len(new_visited), helper(i + 1, new_visited))
            if i - start >= D:
                break
        return max_length

    max_length = 0
    for i in range(n):
        max_length = max(max_length, helper(i, []))
    return max_length

# Input parsing
n, D, M = map(int, input().split())
array = list(map(int, input().split()))

result = longest_exploration_sequence(n, D, M, array)
print(result)
```
