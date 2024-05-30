
import sys

def solve(n, c, s, f):
    # Write your code here
    for i in range(1, n):
        s[i] += s[i - 1]
    for i in range(1, n):
        s[i] += f[i - 1] * (s[i - 1] // f[i - 1])
    for i in range(1, n):
        s[i] += c[i - 1]
    return s

n = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))
s = list(map(int, sys.stdin.readline().split()))
f = list(map(int, sys.stdin.readline().split()))
print('\n'.join(map(str, solve(n, c, s, f))))

