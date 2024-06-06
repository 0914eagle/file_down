
#https://codeforces.com/problemset/problem/1155/B

from sys import stdin
from collections import deque

word = [ch for ch in stdin.readline().strip().lower()]

w = deque(word)

n = len(word)

m = 0

while n != 0:
    n -= 1
    x = w.popleft()
    if x == 'o':
        m += 1
        if m == 15:
            print('YES')
            exit()
    else:
        m = 0

print('NO')
