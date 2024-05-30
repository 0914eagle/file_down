
def fahrenheit_to_celsius(fahrenheit):
    a, b = fahrenheit.split("/")
    a, b = int(a), int(b)
    return str(int(((a-32)*5)/9)) + "/" + str(b)

fahrenheit = input()
print(fahrenheit_to_celsius(fahrenheit))

