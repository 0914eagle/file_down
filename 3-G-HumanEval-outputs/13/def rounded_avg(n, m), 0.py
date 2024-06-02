
def rounded_avg(n, m):
    if n > m:
        return -1
    avg = (n + m) / 2
    rounded_avg = round(avg)
    return bin(rounded_avg)

# Test cases
print(rounded_avg(1, 5))  # Output: 0b11
print(rounded_avg(7, 5))  # Output: -1
print(rounded_avg(10, 20))  # Output: 0b1111
print(rounded_avg(20, 33))  # Output: 0b11010
