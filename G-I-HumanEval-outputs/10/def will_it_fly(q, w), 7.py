
def will_it_fly(q, w):
    # Check if the list q is palindromic
    if q != q[::-1]:
        return False
    
    # Check if the sum of elements in q is less than or equal to the maximum weight w
    if sum(q) <= w:
        return True
    else:
        return False

# Test cases
print(will_it_fly([1, 2], 5))  # ➞ False
print(will_it_fly([3, 2, 3], 1))  # ➞ False
print(will_it_fly([3, 2, 3], 9))  # ➞ True
print(will_it_fly([3], 5))  # ➞ True
```
