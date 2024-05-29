
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    
    if end1 < start2 or end2 < start1:
        return "NO"
    
    start_intersection = max(start1, start2)
    end_intersection = min(end1, end2)
    
    length = end_intersection - start_intersection + 1
    
    if length <= 1:
        return "NO"
    
    if is_prime(length):
        return "YES"
    else:
        return "NO"

# Example tests
print(intersection((1, 2), (2, 3)))  # "NO"
print(intersection((-1, 1), (0, 4)))  # "NO"
print(intersection((-3, -1), (-5, 5)))  # "YES"
```
