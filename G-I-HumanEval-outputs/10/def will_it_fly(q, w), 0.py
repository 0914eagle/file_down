
def will_it_fly(q, w):
    # Check if the object is balanced (palindromic list)
    if q != q[::-1]:
        return False

    # Check if the sum of elements is less than or equal to the maximum possible weight
    if sum(q) <= w:
        return True
    else:
        return False

# Test cases
print(will_it_fly([1, 2], 5))  # Output: False
print(will_it_fly([3, 2, 3], 1))  # Output: False
print(will_it_fly([3, 2, 3], 9))  # Output: True
print(will_it_fly([3], 5))  # Output: True
```
