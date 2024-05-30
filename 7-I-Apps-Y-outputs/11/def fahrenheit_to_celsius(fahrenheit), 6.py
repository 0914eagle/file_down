
def fahrenheit_to_celsius(fahrenheit):
    numerator, denominator = fahrenheit.split("/")
    numerator = int(numerator)
    denominator = int(denominator)
    numerator = (9 * numerator) / 5 + 32
    gcd = gcd_of_two_numbers(numerator, denominator)
    numerator /= gcd
    denominator /= gcd
    return str(numerator) + "/" + str(denominator)

def gcd_of_two_numbers(a, b):
    if b == 0:
        return a
    else:
        return gcd_of_two_numbers(b, a % b)

fahrenheit = input()
print(fahrenheit_to_celsius(fahrenheit))

