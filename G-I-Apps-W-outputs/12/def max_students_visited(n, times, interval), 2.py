
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

# Read input
n = int(input())
times = list(map(int, input().split()))
interval = int(input())

# Call the function and print the output
print(max_students_visited(n, times, interval))
