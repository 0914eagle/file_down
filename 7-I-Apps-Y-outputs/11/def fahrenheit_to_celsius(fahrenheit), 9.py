
def fahrenheit_to_celsius(fahrenheit):
    numerator, denominator = fahrenheit.split('/')
    numerator = int(numerator)
    denominator = int(denominator)
    if denominator == 0:
        return fahrenheit
    if numerator < 0:
        numerator = -9 * numerator
        denominator = 5 * denominator
        return str(numerator) + '/' + str(denominator)
    numerator = 9 * numerator
    denominator = 5 * denominator
    return str(numerator) + '/' + str(denominator)

fahrenheit = input()
print(fahrenheit_to_celsius(fahrenheit))

