
import re

def is_valid_roman_numeral(roman_num):
    pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    return bool(re.match(pattern, roman_num))

# Input
roman_num = input().strip()

# Output
print(is_valid_roman_numeral(roman_num))
