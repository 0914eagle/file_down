
import re
pattern = "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

def is_valid_roman(num):
    if re.match(pattern, num):
        return True
    return False

if __name__ == '__main__':
    num = input()
    print(is_valid_roman(num))

