
from sys import stdin

def search(t, s):
    n, m = map(int, stdin.readline().split())
    t = [tuple(map(int, x.split("-"))) for x in stdin.readline().split()]
    s = [tuple(map(int, x.split("-"))) for x in stdin.readline().split()]
    res = 0
    for i in range(n - m + 1):
        j = 0
        while j < m and t[i + j][1] == s[j][1]:
            j += 1
        if j == m:
            res += 1
    return res

print(search(t, s))

