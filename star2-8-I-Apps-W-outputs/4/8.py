
import sys
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    n, m = map(int, readline().split())
    print(math.factorial(m - 1) % (10**9 + 7))


if __name__ == '__main__':
    main()

