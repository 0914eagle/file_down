
def even_odd_count(num):
    num = abs(num)  # Take the absolute value to handle negative numbers
    even_count = 0
    odd_count = 0

    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num = num // 10

    return even_count, odd_count

# Test cases
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))  # Output: (1, 2)