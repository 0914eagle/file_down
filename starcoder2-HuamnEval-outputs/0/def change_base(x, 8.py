
 def change_base(x: int, base: int):
    
    if x < 0:
        is_negative = True
        x = -x
    else:
        is_negative = False
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x = x // base
    if is_negative:
        digits.append('-')
    return ''.join(reversed(digits))
 