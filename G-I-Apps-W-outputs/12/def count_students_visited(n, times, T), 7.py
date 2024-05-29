
def count_students_visited(n, times, T):
    times.sort()
    visited = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n and times[j] - times[i] <= T:
            j += 1
        visited = max(visited, j - i)
        i += 1
    return visited

n = int(input())
times = list(map(int, input().split()))
T = int(input())

result = count_students_visited(n, times, T)
print(result)
```
