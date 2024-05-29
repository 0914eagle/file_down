
def will_it_fly(q, w):
    # Check if the list is palindromic
    if q == q[::-1]:
        # Check if the sum of elements is less than or equal to w
        if sum(q) <= w:
            return True
    return False

# Test cases
print(will_it_fly([1, 2], 5)) # False
print(will_it_fly([3, 2, 3], 1)) # False
print(will_it_fly([3, 2, 3], 9)) # True
print(will_it_fly([3], 5)) # True
```
