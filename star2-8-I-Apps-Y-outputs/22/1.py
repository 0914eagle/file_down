
import re

def is_valid_roman(s):
    regex = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
    return regex.match(s) is not None

print(is_valid_roman(input()))

