
def longest_exploration(n, D, M, nums):
    def dfs(pos, visited):
        max_length = 1
        for i in range(n):
            if not visited[i] and abs(nums[pos] - nums[i]) <= M and abs(pos - i) <= D:
                visited[i] = True
                max_length = max(max_length, 1 + dfs(i, visited))
                visited[i] = False
        return max_length

    max_length = 0
    for i in range(n):
        visited = [False] * n
        visited[i] = True
        max_length = max(max_length, dfs(i, visited))

    return max_length

# Input processing
n, D, M = map(int, input().split())
nums = list(map(int, input().split()))

# Calculate and output the length of the longest exploration sequence
print(longest_exploration(n, D, M, nums))
```
