def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''
 
 ```python
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

def is_odd(num):
    return num % 2 != 0

def is_even(num):
    return num % 2 == 0

def is_divisible(num1, num2):
    return num1 % num2 == 0

def is_palindrome(string):
    return string == string[::-1]

def is_square(num):
    return num ** 0.5 % 1 == 0

def is_cube(num):
    return num ** (1/3) % 1 == 0

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def is_armstrong(num):
    return sum([int(i) ** len(str(num)) for i in str(num)]) == num

def is_disarium(num):
    return sum([int(i) ** (index + 1) for index, i in enumerate(str(num))]) == num

def is_triangular(num):
    return 0.5 * num * (num + 1) % 1 == 0

def is_perfect(num):
    return sum([i for i in range(1, num) if num % i == 0]) == num

def is_abundant(num):
    return sum([i for i in range(1, num) if num % i == 0]) > num

def is_deficient(num):
    return sum([i for i in range(1, num) if num % i == 0]) < num

def is_prime_palindrome(num):
    return is_prime(num) and is_palindrome(str(num))

def is_prime_square(num):
    return is_prime(num) and is_square(num)

def is_prime_cube(num):
    return is_prime(num) and is_cube(num)

def is