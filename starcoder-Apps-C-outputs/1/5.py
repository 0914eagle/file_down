
# 链接：https://www.acwing.com/problem/content/2529/

# 思路：
# 若数字n经过了K次循环，则可以看出1~9 循环的次数为 1, 2, 6, 6, 3, 1, 1, 0, 0，
# 先循环除以 7，看余数，再根据余数推出循环次数。
# 循环次数为10的倍数的数，最后的数都是1，否则循环次数取模10后得出最后的数。

import sys
from collections import defaultdict

def solve(n):
    ans = [0] * 9
    if n % 7 == 0:
        return 1, 1
    elif n % 7 == 1 or n % 7 == 2 or n % 7 == 3:
        return 1, n
    elif n % 7 == 4 or n % 7 == 5:
        return 2, n
    else:
        return 6, n

def main():
    l, r = map(int, sys.stdin.readline().strip().split())
    ans = [0] * 9
    for n in range(l, r+1):
        k, t = solve(n)
        if k % 10 == 0:
            ans[1] += 1
        else:
            ans[t % 10] += 1
    for i in range(9):
        print(ans[i], end=' ')

if __name__ == '__main__':
    main()
