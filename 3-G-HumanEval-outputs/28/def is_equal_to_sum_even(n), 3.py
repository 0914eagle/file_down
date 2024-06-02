
def is_equal_to_sum_even(n):
    if n % 2 != 0:
        return False
    for i in range(1, n//2 + 1):
        for j in range(i, n//2 + 1):
            for k in range(j, n//2 + 1):
                for l in range(k, n//2 + 1):
                    if 2*i + 2*j + 2*k + 2*l == n:
                        return True
    return False

# Test cases
print(is_equal_to_sum_even(4))  # False
print(is_equal_to_sum_even(6))  # False
print(is_equal_to_sum_even(8))  # True
