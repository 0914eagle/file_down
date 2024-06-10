
import re
def roman_validation(string):
    regex = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return bool(re.match(regex, string))
if __name__ == "__main__":
    string = input()
    print(roman_validation(string))

