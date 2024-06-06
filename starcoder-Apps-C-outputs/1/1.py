
#!/usr/bin/env python3

import math
import sys

def digit_product(n):
    return 1 if n == 0 else n * digit_product(n % 10)

def main():
    L, R = [int(i) for i in sys.stdin.read().split()]
    results = [0] * 9
    for i in range(L, R+1):
        n = digit_product(i)
        while n >= 10:
            n = digit_product(n)
        results[n - 1] += 1
    for r in results:
        print(r, end=' ')

if __name__ == '__main__':
    main()
