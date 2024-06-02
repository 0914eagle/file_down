
def is_equal_to_sum_even(n):
    if n % 2 != 0:
        return False
    for i in range(1, n//2 + 1):
        for j in range(i, n//2 + 1):
            for k in range(j, n//2 + 1):
                for l in range(k, n//2 + 1):
                    if i + j + k + l == n and i % 2 == 0 and j % 2 == 0 and k % 2 == 0 and l % 2 == 0:
                        return True
    return False

# Test cases
print(is_equal_to_sum_even(4))  # False
print(is_equal_to_sum_even(6))  # False
print(is_equal_to_sum_even(8))  # True
