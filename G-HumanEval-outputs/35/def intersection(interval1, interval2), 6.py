
def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2

    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)

    if intersection_start > intersection_end:
        return "NO"

    length = intersection_end - intersection_start + 1

    if length < 2:
        return "NO"

    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return "NO"

    return "YES"

# Test cases
print(intersection((1, 2), (2, 3)))  # Output: NO
print(intersection((-1, 1), (0, 4)))  # Output: NO
print(intersection((-3, -1), (-5, 5)))  # Output: YES
```
