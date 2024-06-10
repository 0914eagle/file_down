
from sys import stdin


def fairness(n):
    return n * (n+1) // 2


t = int(stdin.readline().rstrip())
for _ in range(t):
    n = int(stdin.readline().rstrip())
    print(fairness(n))

