
from sys import stdin

def getln():
    return stdin.readline()

def geti():
    return int(getln())

def getii():
    return list(map(int, getln().split()))

def getiii():
    return list(map(int, getln().split()))

def getn(n):
    return [getii() for _ in range(n)]

def put(s):
    print(s)

def puti(n):
    print(n)

def putii(a, b):
    print(a, b)

def putiii(a, b, c):
    print(a, b, c)

def putn(a):
    print('\n'.join(a))

def ctoi(c):
    return ord(c) - ord('0')

def itoc(i):
    return chr(i + ord('0'))

def iits(x):
    s = []
    while x > 0:
        s.append(itoc(x % 10))
        x //= 10
    return ''.join(reversed(s))

def getdis(l, r):
    return l + (r - l) // 2

def solve(n, r, p):
    l, r = 1, n
    while l <= r:
        dis = getdis(l, r)
        time = dis * p
        if time < r:
            l = dis + 1
        else:
            r = dis - 1
    return l * p

puti(solve(*getii()))
