
import re

roman_pattern = r'^(?=[MDCLXVI])M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

def is_roman_numeral(numeral):
    return bool(re.match(roman_pattern, numeral))

numeral = input()
print(is_roman_numeral(numeral))

