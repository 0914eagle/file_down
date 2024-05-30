
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def convert_to_lowest_terms(numerator, denominator):
    gcd = gcd(numerator, denominator)
    return (numerator / gcd, denominator / gcd)

def fahrenheit_to_celsius_lowest_terms(fahrenheit):
    numerator = fahrenheit_to_celsius(fahrenheit) * fahrenheit.denominator
    denominator = fahrenheit.numerator
    return convert_to_lowest_terms(numerator, denominator)

fahrenheit = Fraction(input())
print(fahrenheit_to_celsius_lowest_terms(fahrenheit))

