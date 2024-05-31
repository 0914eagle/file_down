
def even_odd_count(num):
    num_str = str(abs(num))
    even_count = 0
    odd_count = 0

    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if num < 0:
        return (even_count, odd_count)
    else:
        return (odd_count, even_count)

# Test cases
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))  # Output: (1, 2)
