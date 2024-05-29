
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    if start1 > end2 or end1 < start2:
        return "NO"  # No intersection
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    intersection_length = intersection_end - intersection_start
    
    if intersection_length < 0:
        return "NO"  # No intersection
    elif is_prime(intersection_length):
        return "YES"
    else:
        return "NO"

# Test cases
print(intersection((1, 2), (2, 3)))  # ==> "NO"
print(intersection((-1, 1), (0, 4)))  # ==> "NO"
print(intersection((-3, -1), (-5, 5)))  # ==> "YES"
```
