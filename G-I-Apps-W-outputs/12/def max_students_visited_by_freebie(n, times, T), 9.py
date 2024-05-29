
def max_students_visited_by_freebie(n, times, T):
    times.sort()
    count = 1
    max_count = 1

    for i in range(1, n):
        if times[i] - times[i-1] <= T:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1

    return max_count

n = int(input())
times = list(map(int, input().split()))
T = int(input())

result = max_students_visited_by_freebie(n, times, T)
print(result)
```
