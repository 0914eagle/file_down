
def double_the_difference(lst):
    total = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            total += num ** 2
    return total * 2

# Test cases
print(double_the_difference([1, 3, 2, 0]))  # Output should be 10
print(double_the_difference([-1, -2, 0]))  # Output should be 0
print(double_the_difference([9, -2]))  # Output should be 81
print(double_the_difference([0]))  # Output should be 0
print(double_the_difference([]))  # Output should be 0
