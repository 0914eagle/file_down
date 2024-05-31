
def minimum_hours_to_water_garden(n, k, buckets):
    min_hours = float('inf')
    for i in range(n):
        if k % buckets[i] == 0:
            hours = k // buckets[i]
            min_hours = min(min_hours, hours)
    
    return min_hours

# Input
n, k = map(int, input().split())
buckets = list(map(int, input().split()))

# Output
print(minimum_hours_to_water_garden(n, k, buckets))
