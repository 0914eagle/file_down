
def is_equal_to_sum_even(n):
    if n % 2 != 0:
        return False
    half_n = n // 2
    for i in range(1, half_n // 2 + 1):
        if half_n % i == 0 and half_n // i % 2 == 0:
            return True
    return False

# Test cases
print(is_equal_to_sum_even(4))  # False
print(is_equal_to_sum_even(6))  # False
print(is_equal_to_sum_even(8))  # True
