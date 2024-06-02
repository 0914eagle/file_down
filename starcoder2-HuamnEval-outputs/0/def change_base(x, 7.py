
 def change_base(x: int, base: int):
    
    if x == 0:
        return '0'
    digits = '0123456789ABCDEF'
    if x < 0:
        sign = '-'
        x = -x
    else:
        sign = ''
    while x:
        sign += digits[x % base]
        x = x // base
    return sign[::-1]
