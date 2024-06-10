
import math

def max_offices(digits):
    if digits == 1:
        return 2
    if digits == 2:
        return 6
    n_digits = digits - 2
    max_lucky_num = int('8' * n_digits + '77')
    return math.ceil(max_lucky_num / 2)

print(max_offices(int(input())))

