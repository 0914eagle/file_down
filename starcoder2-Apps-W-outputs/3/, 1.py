
# -*- coding: utf-8 -*-
# @Date    : 2018-08-29 16:31:13
# @Author  : xiaok
# @Version : 1.0

import sys

def main():
    s = sys.stdin.readline().strip()
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            a = int(s[:i])
            b = int(s[i:j])
            c = int(s[j:])
            if a + b == c:
                print(a, '+', b, '=', c, sep='')
                return
    print('No solution')

if __name__ == "__main__":
    main()
