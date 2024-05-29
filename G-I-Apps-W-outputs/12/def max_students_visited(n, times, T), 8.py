
def max_students_visited(n, times, T):
    times.sort()
    max_students = 0
    for i in range(n):
        count = 1
        j = i + 1
        while j < n and times[j] - times[i] <= T:
            count += 1
            j += 1
        max_students = max(max_students, count)
    return max_students

# Input
n = 6
times = [4, 1, 7, 8, 3, 8]
T = 1

# Output
print(max_students_visited(n, times, T))
```
