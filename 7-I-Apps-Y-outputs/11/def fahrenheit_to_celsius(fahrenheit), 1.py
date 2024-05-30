
def fahrenheit_to_celsius(fahrenheit):
    celsius = 9.0/5.0 * fahrenheit - 32
    return celsius

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def convert_to_lowest_terms(numerator, denominator):
    gcd = gcd(numerator, denominator)
    return numerator / gcd, denominator / gcd

fahrenheit = input()
fahrenheit_list = fahrenheit.split("/")
numerator = int(fahrenheit_list[0])
denominator = int(fahrenheit_list[1])
celsius = fahrenheit_to_celsius(fahrenheit)
celsius_numerator = int(celsius * denominator)
celsius_denominator = denominator
celsius_numerator, celsius_denominator = convert_to_lowest_terms(celsius_numerator, celsius_denominator)
print(celsius_numerator, "/", celsius_denominator)

