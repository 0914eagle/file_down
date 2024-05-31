
import re

def is_valid_roman_numeral(s):
    pattern = "^M*(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return bool(re.match(pattern, s))

# Test the function
input_str = input().strip()
print(is_valid_roman_numeral(input_str))