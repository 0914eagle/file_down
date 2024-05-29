
def max_students_visited(n, times, T):
    times.sort()
    count = 0
    i = 0
    while i < n:
        j = i
        while j < n - 1 and times[j + 1] - times[i] <= T:
            j += 1
        count = max(count, j - i + 1)
        i += 1
    return count

# Input
n = int(input())
times = list(map(int, input().split()))
T = int(input())

# Output
print(max_students_visited(n, times, T))
```
