
import sys

n, m, c = map(int, sys.stdin.readline().split())
b = list(map(int, sys.stdin.readline().split()))

codes = []
for _ in range(n):
    codes.append(list(map(int, sys.stdin.readline().split())))

count = 0
for code in codes:
    if sum([code[i] * b[i] for i in range(m)]) + c > 0:
        count += 1

print(count)

