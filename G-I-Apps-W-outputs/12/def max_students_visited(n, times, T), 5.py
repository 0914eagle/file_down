
def max_students_visited(n, times, T):
    times.sort()
    max_students = 0
    for i in range(n):
        count = 1
        for j in range(i + 1, n):
            if times[j] - times[i] <= T:
                count += 1
            else:
                break
        if count > max_students:
            max_students = count
    return max_students

# Input processing
n = int(input())
times = list(map(int, input().split()))
T = int(input())

# Call the function and print the result
print(max_students_visited(n, times, T))
```
