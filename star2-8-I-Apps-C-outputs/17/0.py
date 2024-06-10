
from sys import stdin
n, k = [int(x) for x in stdin.readline().split()]
s = "1" * k
if n != k:
    s += "0" * (n - k)
print(s)

