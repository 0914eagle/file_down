
import math
import random
import itertools
import sys

def solve():
    n, d, c = [int(x) for x in sys.stdin.readline().strip().split()]
    if c == 0:
        return 1
    elif c == 1:
        return 1.0 * (n - 1) / n
    elif c >= n:
        return 0
    elif c == 2:
        return 1.0 * (n - 1) * (n - 2) / n / (n - 1)

    state = {}

    def dfs(board):
        if str(board) in state:
            return state[str(board)]
        ans = 0
        if board == n - c:
            return 0
        if board == 0:
            return 1
        for i in itertools.combinations(range(n - 1), d - 1):
            if board in i:
                continue
            i = list(i)
            i.append(board)
            i.sort()
            ans += dfs(board + 1) / math.factorial(d) * 1.0
        state[str(board)] = ans
        return ans

    return dfs(0)


print(solve())
