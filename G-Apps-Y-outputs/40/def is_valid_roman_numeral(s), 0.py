
import re

def is_valid_roman_numeral(s):
    pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    return bool(re.match(pattern, s))

# Test the function with some examples
print(is_valid_roman_numeral("III"))  # True
print(is_valid_roman_numeral("IV"))   # True
print(is_valid_roman_numeral("CDXCIX"))  # True
print(is_valid_roman_numeral("XIIII"))  # False
print(is_valid_roman_numeral("MMMMM"))  # False
