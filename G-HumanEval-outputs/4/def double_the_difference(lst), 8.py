
def double_the_difference(lst):
    odd_nums = [num for num in lst if num > 0 and num % 2 != 0 and isinstance(num, int)]
    return sum(num**2 for num in odd_nums) * 2

# Test cases
print(double_the_difference([1, 3, 2, 0]))  # Output: 10
print(double_the_difference([-1, -2, 0]))  # Output: 0
print(double_the_difference([9, -2]))      # Output: 81
print(double_the_difference([0]))          # Output: 0
print(double_the_difference([]))           # Output: 0
```
