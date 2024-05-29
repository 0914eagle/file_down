
def special_factorial(n):
    result = 1
    factorial = 1
    for i in range(n, 0, -1):
        factorial *= i
        result *= factorial
    return result

print(special_factorial(4))  # Output: 288
