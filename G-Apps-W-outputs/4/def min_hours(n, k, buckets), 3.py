
def min_hours(n, k, buckets):
    min_hours = float('inf')
    for bucket in buckets:
        if k % bucket == 0:
            min_hours = min(min_hours, k // bucket)
    return min_hours

# Input parsing
n, k = map(int, input().split())
buckets = list(map(int, input().split()))

# Output
print(min_hours(n, k, buckets))
