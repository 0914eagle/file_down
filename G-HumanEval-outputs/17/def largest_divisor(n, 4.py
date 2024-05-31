
def largest_divisor(n: int) -> int:
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i

# Test the function with the example
print(largest_divisor(15))
