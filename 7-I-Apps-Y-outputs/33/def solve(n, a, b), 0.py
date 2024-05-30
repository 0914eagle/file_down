
import itertools
import string


def solve(n, a, b):
    s = string.ascii_lowercase
    ans = ''
    for i in range(n):
        ans += s[i % len(s)]
    return ans


def main():
    t = int(input())
    for i in range(t):
        n, a, b = map(int, input().split())
        print(solve(n, a, b))


if __name__ == "__main__":
    main()

