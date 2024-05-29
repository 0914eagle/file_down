
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    
    if end1 < start2 or end2 < start1:
        return "NO"
    
    intersect_start = max(start1, start2)
    intersect_end = min(end1, end2)
    
    intersect_length = intersect_end - intersect_start
    
    if intersect_length <= 0:
        return "NO"
    
    if is_prime(intersect_length):
        return "YES"
    else:
        return "NO"

# Test cases
print(intersection((1, 2), (2, 3)))  # "NO"
print(intersection((-1, 1), (0, 4)))  # "NO"
print(intersection((-3, -1), (-5, 5)))  # "YES"
```
