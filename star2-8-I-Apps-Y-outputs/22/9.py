
import re
regex = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

def is_roman(num):
    if re.match(regex, num):
        return True
    return False

if __name__ == '__main__':
    num = input()
    print(is_roman(num))

