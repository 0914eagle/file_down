
# O(N)

import sys

n = int(input())
max_size = 0
total_size = 0
last_sent = 0
for i in range(n):
    ti, ci = [int(x) for x in sys.stdin.readline().split()]
    if ti - last_sent >= max_size:
        max_size = ti - last_sent
    total_size += ci
    if total_size > max_size:
        max_size = total_size
    if ti > last_sent:
        last_sent = ti

print(last_sent + max_size, max_size)
