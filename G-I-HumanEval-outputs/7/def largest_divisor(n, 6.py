
def largest_divisor(n: int) -> int:
    
    if n <= 1:
        return None
    
    largest = 1
    for i in range(2, n):
        if n % i == 0:
            largest = i

    return largest

print(largest_divisor(15))  # Output: 5
``` 
