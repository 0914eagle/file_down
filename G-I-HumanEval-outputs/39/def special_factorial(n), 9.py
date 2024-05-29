
def special_factorial(n):
    result = 1
    factorial = 1
    
    while n > 0:
        factorial *= n
        result *= factorial
        n -= 1
        
    return result

print(special_factorial(4))  # Output: 288
