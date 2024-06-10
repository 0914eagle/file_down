
import sys
from itertools import combinations

def solve():
    n = int(input())
    s = [int(input()) for _ in range(n)]
    best = -1
    for a, b, c in combinations(s, 3):
        best = max(best, a + b + c)
    if best > 0:
        print(best)
    else:
        print('no solution')

if __name__ == '__main__':
    solve()

