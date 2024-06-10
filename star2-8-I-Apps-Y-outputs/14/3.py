
import math

x = int(input())
for i in range(1, x + 1):
    for j in range(2, x + 1):
        if i ** j <= x:
            max_power = i ** j
print(max_power)

