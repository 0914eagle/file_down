
# -*- coding: utf-8 -*-


import numpy as np

def main():
    x, y, x0, y0 = map(int, input().split())
    s = input()
    n = len(s)
    ans = np.zeros(n+1, dtype=int)
    ans[0] = 1
    for i in range(n):
        if s[i] == 'U':
            x0 -= 1
        elif s[i] == 'D':
            x0 += 1
        elif s[i] == 'L':
            y0 -= 1
        else:
            y0 += 1
        ans[i+1] = ans[i]
        if x0 < 1 or x0 > x or y0 < 1 or y0 > y:
            ans[i+1] -= 1
    print(*ans)

if __name__ == '__main__':
    main()
