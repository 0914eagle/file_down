
# -*- coding: utf-8 -*-

# @Date    : 2018-09-06 10:04:03
# @Author  :  ()
# @Link    : link
# @Version : 1.0.0

from sys import stdin

max_n = 100

def read_list():
    return [int(x) for x in stdin.readline().split()]

def read_line():
    return stdin.readline().strip()

def read_int():
    return int(stdin.readline())


def main():
    t = read_int()
    for _ in range(t):
        k = read_int()
        s = read_line()
        ans = 0
        for i in range(k):
            if s[i] == 'A':
                ans = max(ans, i + 1)
        print(ans)


if __name__ == '__main__':
    main()
