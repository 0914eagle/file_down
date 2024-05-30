
def fahrenheit_to_celsius(fahrenheit):
    numerator, denominator = fahrenheit.split("/")
    numerator = int(numerator)
    denominator = int(denominator)
    return str(int((9*numerator)/denominator - 32)) + "/" + str(denominator)

def main():
    fahrenheit = input()
    print(fahrenheit_to_celsius(fahrenheit))

if __name__ == "__main__":
    main()

