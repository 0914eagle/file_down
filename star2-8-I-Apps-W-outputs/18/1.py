
import sys
input = sys.stdin.readline


def main():
    n, a, b = map(int, input().split())
    h = [int(input()) for _ in range(n)]

    left, right = 0, 10**18
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid, n, a, b, h):
            right = mid
        else:
            left = mid

    print(right)


def check(x, n, a, b, h):
    for i in range(n):
        h[i] -= b * x
    for i in range(n):
        if h[i] > 0:
            x = (h[i] + a - b - 1) // (a - b)
            for j in range(n):
                h[j] -= b * x
            break

    return all(hi <= 0 for hi in h)


if __name__ == '__main__':
    main()


