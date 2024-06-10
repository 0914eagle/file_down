
import sys

def solve(perm, ops):
    n = len(perm)
    inv = [0] * (n + 1)
    for i in range(n):
        inv[perm[i]] = i

    for a, b in ops:
        a, b = inv[a], inv[b]
        perm[a], perm[b] = perm[b], perm[a]
        inv[perm[a]], inv[perm[b]] = a, b

    return perm


def main():
    n, m = map(int, sys.stdin.readline().split())
    perm = list(map(int, sys.stdin.readline().split()))
    ops = []
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        ops.append((a, b))
    result = solve(perm, ops)
    print(*result)


if __name__ == '__main__':
    main()

