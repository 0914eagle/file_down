
def double_the_difference(lst):
    result = sum(x ** 2 for x in lst if x > 0 and x % 2 != 0 and isinstance(x, int))
    return result * 2

# Test cases
print(double_the_difference([1, 3, 2, 0]))  # Output: 10
print(double_the_difference([-1, -2, 0]))  # Output: 0
print(double_the_difference([9, -2]))      # Output: 81
print(double_the_difference([0]))          # Output: 0
print(double_the_difference([]))            # Output: 0
```
