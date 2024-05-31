
import re

def validate_roman_numeral(s):
    pattern = "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return bool(re.match(pattern, s))

# Test the function
numeral = input().strip()
print(validate_roman_numeral(numeral))
