
def longest_exploration_sequence(n, D, M, array):
    def explore(start):
        visited = set()
        current = start
        visited.add(current)
        while True:
            found_next = False
            for i in range(max(0, current - D), min(n, current + D + 1)):
                if i != current and abs(array[i] - array[current]) <= M and i not in visited:
                    visited.add(i)
                    current = i
                    found_next = True
                    break
            if not found_next:
                break
        return len(visited)

    max_sequence = 0
    for start in range(n):
        max_sequence = max(max_sequence, explore(start))

    return max_sequence

# Input processing
n, D, M = map(int, input().split())
array = list(map(int, input().split()))

# Call the function and print the result
result = longest_exploration_sequence(n, D, M, array)
print(result)
```
