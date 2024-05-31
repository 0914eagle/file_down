
def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2

    # Check if the intervals intersect
    if end1 < start2 or end2 < start1:
        return "NO"

    # Calculate the intersection interval
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)

    # Calculate the length of the intersection interval
    intersection_length = intersection_end - intersection_start + 1

    # Check if the length is a prime number
    if intersection_length <= 1:
        return "NO"
    for i in range(2, int(intersection_length ** 0.5) + 1):
        if intersection_length % i == 0:
            return "NO"
    return "YES"

# Test cases
print(intersection((1, 2), (2, 3)))  # "NO"
print(intersection((-1, 1), (0, 4)))  # "NO"
print(intersection((-3, -1), (-5, 5)))  # "YES"
```
