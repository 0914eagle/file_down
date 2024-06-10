
import sys

def solve(n, a, b, h):
    h.sort(reverse=True)
    res = 0
    for i in range(n):
        if h[i] <= b:
            break
        res += h[i] // b
        if h[i] % b >= a:
            res += 1
            h[i] = 0
    return res

def main():
    n, a, b = map(int, input().split())
    h = [int(x) for x in sys.stdin.read().split()]
    print(solve(n, a, b, h))

if __name__ == '__main__':
    main()

