
import re

def validate_roman_numeral(roman_num):
    pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    if re.match(pattern, roman_num):
        print(True)
    else:
        print(False)

# Input
roman_numeral = input().strip()

# Validate Roman numeral
validate_roman_numeral(roman_numeral)
