
import sys
import heapq

def update(a: int, b: int) -> None:
    for i in range(a, n + 1):
        hq[i] += abs(i - a) + b

def evaluate() -> None:
    x = min(hq)
    print(x, hq[x])

input = sys.stdin.readline

q = int(input())

hq = [0] * (10 ** 9 + 1)
n = len(hq) - 1

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        update(query[1], query[2])
    else:
        evaluate()

