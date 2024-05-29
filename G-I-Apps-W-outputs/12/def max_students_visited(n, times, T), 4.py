
def max_students_visited(n, times, T):
    times.sort()
    visited = 0
    for i in range(n):
        j = i + 1
        while j < n and times[j] - times[i] <= T:
            visited = max(visited, j - i + 1)
            j += 1
    return visited

# Input processing
n = int(input())
times = list(map(int, input().split()))
T = int(input())

# Call the function and print the result
print(max_students_visited(n, times, T))
