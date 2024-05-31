
def min_hours(n, k, buckets):
    min_hours = k
    for bucket in buckets:
        if k % bucket == 0:
            min_hours = min(min_hours, k // bucket)
    return min_hours

# Read input
n, k = map(int, input().split())
buckets = list(map(int, input().split()))

# Output result
print(min_hours(n, k, buckets))
