
def calculate_min_distance_sum(n, coordinates, speeds):
    coordinates_sorted = sorted(zip(coordinates, speeds))
    total_sum = 0
    current_sum = 0
    for i in range(n - 1):
        total_sum += current_sum
        current_sum += (coordinates_sorted[i+1][0] - coordinates_sorted[i][0]) * coordinates_sorted[i][1] + current_sum * (n-i-1)
    return total_sum

# Input
n = int(input())
coordinates = list(map(int, input().split()))
speeds = list(map(int, input().split()))

# Output
print(calculate_min_distance_sum(n, coordinates, speeds))
