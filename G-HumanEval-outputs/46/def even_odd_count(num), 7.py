
def even_odd_count(num):
    num_str = str(abs(num))
    even_count = sum(1 for digit in num_str if int(digit) % 2 == 0)
    odd_count = len(num_str) - even_count
    return (even_count, odd_count)

# Test cases
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))  # Output: (1, 2)
