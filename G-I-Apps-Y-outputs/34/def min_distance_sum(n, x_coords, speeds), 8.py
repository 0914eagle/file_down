
def min_distance_sum(n, x_coords, speeds):
    total_sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if speeds[i] == speeds[j]:
                total_sum += abs(x_coords[i] - x_coords[j])
            else:
                total_sum += min(abs(x_coords[i] - x_coords[j]) / abs(speeds[i] - speeds[j]),
                                  abs(x_coords[j] - x_coords[i]) / abs(speeds[i] - speeds[j]))
    return total_sum

# Read input
n = int(input())
x_coords = list(map(int, input().split()))
speeds = list(map(int, input().split()))

# Call the function and print the result
print(min_distance_sum(n, x_coords, speeds))
```
