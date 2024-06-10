
n = int(input())
cafes = list(map(int, input().split()))
visited = [0] * (2 * 10 ** 5 + 1)
for i in range(n):
    visited[cafes[i]] = i
last = n
for i in range(2 * 10 ** 5 + 1):
    if visited[i] > 0 and last > visited[i]:
        last = visited[i]
print(i)

