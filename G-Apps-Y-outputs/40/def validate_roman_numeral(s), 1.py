
import re

def validate_roman_numeral(s):
    pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    return bool(re.match(pattern, s))

# Test cases
print(validate_roman_numeral("III"))  # True
print(validate_roman_numeral("MMMDCCCLXXXVIII"))  # True
print(validate_roman_numeral("MMMMM"))  # False
print(validate_roman_numeral("XVIIII"))  # False
