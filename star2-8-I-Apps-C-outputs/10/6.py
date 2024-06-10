
import sys
import math
def reverse(n):
    return int(str(n)[::-1])
def number_of_appearances(a, b):
    a = int(a)
    b = int(b)
    a_row = math.floor(math.sqrt(a))
    b_row = math.floor(math.sqrt(b))
    if a_row == b_row:
        return reverse(a)
    if a_row % 2 == 0:
        a_sum = a - a_row * a_row
        a_sum += reverse(a_row)
    else:
        a_sum = reverse(a_row)
        a_sum -= a_row * a_row
        a_sum += a
    if b_row % 2 == 0:
        b_sum = reverse(b_row)
    else:
        b_sum = b - b_row * b_row
        b_sum += reverse(b_row)
    return b_sum - a_sum + 1
for line in sys.stdin:
    a, b = line.split()
    print(number_of_appearances(a, b))

