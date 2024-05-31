
def will_it_fly(q, w):
    if q != q[::-1]:  # Check if the list is not a palindrome
        return False
    if sum(q) > w:  # Check if the sum of elements exceeds maximum weight
        return False
    return True

# Test cases
print(will_it_fly([1, 2], 5))  # ➞ False
print(will_it_fly([3, 2, 3], 1))  # ➞ False
print(will_it_fly([3, 2, 3], 9))  # ➞ True
print(will_it_fly([3], 5))  # ➞ True
```
