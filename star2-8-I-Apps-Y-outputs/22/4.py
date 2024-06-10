
import re

thousand = 'M{,3}'
hundred = '(C[MD]|D?C{,3})'
ten = '(X[CL]|L?X{,3})'
unit = '(I[VX]|V?I{,3})'

pattern = f'^{thousand}{hundred}{ten}{unit}$'

def is_roman_numeral(s):
    return bool(re.match(pattern, s))

print(is_roman_numeral(input()))

