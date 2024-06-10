
import math

def egcd(a, b):
    x, old_x = 0, 1
    y, old_y = 1, 0
    while (b != 0):
        q, r = divmod(a, b)
        a, b = b, r
        x, old_x = old_x - q * x, x
        y, old_y = old_y - q * y, y
    return a, old_x, old_y

n = int(input())

a = [1] + [0] * n
b = [0] * (n + 1)
b[n] = 1

print(n)
print(" ".join(map(str, a)))
print(n + 1)
print(" ".join(map(str, b)))

