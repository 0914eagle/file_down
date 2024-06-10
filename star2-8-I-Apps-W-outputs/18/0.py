
import sys

def solve(n, a, b, h):
    h = sorted(h, reverse=True)
    res = 0
    while len(h) > 0:
        res += 1
        h = [hi - b for hi in h]
        h = [hi for hi in h if hi > 0]
        h = h[:-1] # exclude the strongest monster
    return res

def main():
    tokens = map(int, sys.stdin.readline().split())
    n, a, b = tokens
    h = [int(sys.stdin.readline()) for _ in range(n)]
    print(solve(n, a, b, h))

if __name__ == '__main__':
    main()

