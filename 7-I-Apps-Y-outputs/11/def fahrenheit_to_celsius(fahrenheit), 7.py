
def fahrenheit_to_celsius(fahrenheit):
    a, b = fahrenheit.split('/')
    a, b = int(a), int(b)
    c = (9 * a + 32 * b) / 5
    d = b
    while c % d != 0:
        d += 1
    return str(c // d) + '/' + str(d)

