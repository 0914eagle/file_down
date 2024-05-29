
def largest_divisor(n: int) -> int:
    for i in range(n-1, 1, -1):
        if n % i == 0:
            return i
    return 1

# Test the function
print(largest_divisor(15))  # Output should be 5
``` 
