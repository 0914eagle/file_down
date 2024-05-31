
import re

def validate_roman_numeral(input_str):
    pattern = "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    if re.match(pattern, input_str):
        print(True)
    else:
        print(False)

# Test the function
validate_roman_numeral("III")  # Output: True
validate_roman_numeral("MMMCMXCIX")  # Output: True
validate_roman_numeral("IIII")  # Output: False
