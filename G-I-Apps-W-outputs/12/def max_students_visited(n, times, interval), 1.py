
def max_students_visited(n, times, interval):
    times.sort()
    count = 1
    max_count = 1
    for i in range(1, n):
        if times[i] - times[i-1] <= interval:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1
    return max_count

# Input
n = 6
times = [4, 1, 7, 8, 3, 8]
interval = 1

# Output
print(max_students_visited(n, times, interval))
```
