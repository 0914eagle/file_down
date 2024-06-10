
import math

x = int(input())

max_power = 0
for b in range(1, x + 1):
    for p in range(2, x + 1):
        if b ** p <= x:
            max_power = max(max_power, b ** p)
        else:
            break

print(max_power)

