
def calculate_convenience(n, p):
    cnt = [0] * n
    for i in range(n):
        x = i
        visited = [False] * n
        while not visited[x]:
            visited[x] = True
            x = p[x] - 1
            cnt[i] += 1

    result = 0
    total_sum = sum(cnt)
    for c in cnt:
        result += c * (total_sum - c)

    return result

# Input parsing
n = int(input())
p = list(map(int, input().split()))

# Calculate and print the maximum possible convenience
print(calculate_convenience(n, p))
```
