
def largest_divisor(n: int) -> int:
    # Initialize the largest divisor to 1
    largest = 1
    
    # Iterate from 2 to n//2
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            largest = i
    
    return largest

# Test the function
print(largest_divisor(15))  # Output: 5
