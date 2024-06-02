
def is_equal_to_sum_even(n):
    count = 0
    for i in range(2, n, 2):
        for j in range(2, n, 2):
            for k in range(2, n, 2):
                for l in range(2, n, 2):
                    if i + j + k + l == n:
                        count += 1
    return count == 1

# Test cases
print(is_equal_to_sum_even(4))  # False
print(is_equal_to_sum_even(6))  # False
print(is_equal_to_sum_even(8))  # True
