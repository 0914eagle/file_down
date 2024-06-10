
import re

def check_roman(string):
    regex = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return re.match(regex, string) is not None

if __name__ == "__main__":
    string = input()
    print(check_roman(string))


