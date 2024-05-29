
def largest_divisor(n: int) -> int:
    
    for divisor in range(n - 1, 0, -1):
        if n % divisor == 0:
            return divisor

print(largest_divisor(15))  # Output: 5
``` 
