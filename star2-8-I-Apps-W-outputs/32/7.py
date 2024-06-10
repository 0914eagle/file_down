
import sys


def solve(a, b, n, m):
    def is_possible(order):
        for type in order:
            if type == 1:
                if a > b:
                    a -= 1
                else:
                    b -= 1
            else:
                if a > b:
                    b -= 1
                else:
                    a -= 1
            if a < 0 or b < 0:
                return False
        return True

    for i in range(n + m):
        order = [1] * n + [2] * m
        if is_possible(order):
            return "Yes"
        n, m = m, n
    return "No"


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b, n, m = map(int, sys.stdin.readline().split())
        print(solve(a, b, n, m))


if __name__ == "__main__":
    main()


