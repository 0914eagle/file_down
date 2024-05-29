
def truncate_number(number: float) -> float:
    integer_part = int(number)
    decimal_part = number - integer_part
    return round(decimal_part, 10)  # Rounding to avoid precision issues

# Test cases
print(truncate_number(3.5))  # Output: 0.5
