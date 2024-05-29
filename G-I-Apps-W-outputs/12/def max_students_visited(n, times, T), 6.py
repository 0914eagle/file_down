
def max_students_visited(n, times, T):
    times.sort()
    max_students = 0
    for i in range(n):
        count = 1
        for j in range(i+1, n):
            if times[j] - times[i] <= T:
                count += 1
            else:
                break
        max_students = max(max_students, count)
    return max_students

# Input reading
n = int(input())
times = list(map(int, input().split()))
T = int(input())

result = max_students_visited(n, times, T)
print(result)
```
