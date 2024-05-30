
import sys

N, K = map(int, sys.stdin.readline().split())

d = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

snuke = [0] * N

for i in range(K):
    for j in range(d[i][0], d[i][-1] + 1):
        snuke[j - 1] += 1

print(sum(1 for x in snuke if x == 0))

