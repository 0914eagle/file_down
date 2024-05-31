
def min_hours_to_water_garden(n, k, buckets):
    min_hours = float('inf')
    for bucket in buckets:
        if k % bucket == 0:
            min_hours = min(min_hours, k // bucket)
    return min_hours

n, k = map(int, input().split())
buckets = list(map(int, input().split()))

result = min_hours_to_water_garden(n, k, buckets)
print(result)
