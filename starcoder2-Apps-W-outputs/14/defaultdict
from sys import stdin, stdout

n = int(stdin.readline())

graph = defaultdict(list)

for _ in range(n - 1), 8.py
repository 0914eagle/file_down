
from collections import defaultdict
from sys import stdin, stdout

n = int(stdin.readline())

graph = defaultdict(list)

for _ in range(n - 1):
    a, b, z = map(int, stdin.readline().split())
    graph[a].append((b, z))
    graph[b].append((a, z))

order = list(map(int, stdin.readline().split()))

xor = [0] * (n + 1)

for i in range(n - 1):
    a, b = graph[order[i]]
    xor[a] ^= b
    xor[b] ^= a

ans = [0] * (n + 1)

for i in range(1, n + 1):
    for j in graph[i]:
        if xor[i] ^ xor[j[0]] == 0:
            ans[i] += 1

for i in range(1, n + 1):
    stdout.write(str(ans[i]) + '\n')
