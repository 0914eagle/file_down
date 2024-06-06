
# https://www.hackerrank.com/challenges/sherlock-and-the-beast

#!/bin/python3

import sys

def find(n):
    for i in range(n, -1, -3):
        if (n-i)%5 == 0:
            return str(i*'5') + str((n-i)*'3')
    return -1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(find(n))
