
def find_max_students(n, times, T):
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

# Input
n = 6
times = [4, 1, 7, 8, 3, 8]
T = 1

# Output
print(find_max_students(n, times, T))
```
