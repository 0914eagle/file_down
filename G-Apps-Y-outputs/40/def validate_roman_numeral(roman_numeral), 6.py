
import re

def validate_roman_numeral(roman_numeral):
    pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    if re.match(pattern, roman_numeral):
        print(True)
    else:
        print(False)

# Test the function
validate_roman_numeral("XIV")  # Output: True
validate_roman_numeral("MMMDCCCXLV")  # Output: True
validate_roman_numeral("ABC")  # Output: False
