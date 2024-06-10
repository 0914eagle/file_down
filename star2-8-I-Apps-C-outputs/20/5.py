
from sys import stdin


def solve(s):
    tokens = s.split()
    total = int(tokens[-1])
    if "?" not in s:
        return "Impossible"

    for i in range(1, total + 1):
        for j in range(1, total + 1):
            for k in range(1, total + 1):
                for l in range(1, total + 1):
                    for m in range(1, total + 1):
                        for n in range(1, total + 1):
                            val = i + j - k + l + m
                            if val == total:
                                return f"{i} + {j} - {k} + {l} + {m} = {total}"
    return "Impossible"


s = stdin.readline().strip()
print(solve(s))


