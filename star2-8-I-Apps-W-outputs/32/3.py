
from sys import stdin, stdout


def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        a, b, n, m = map(int, stdin.readline().strip().split())
        if a > b:
            a, b = b, a
            n, m = m, n

        if n > b:
            stdout.write("No\n")
            continue

        while n > 0 and m > 0:
            if a > b:
                a -= 1
                m -= 1
            else:
                b -= 1
                n -= 1

        if n == 0 and m == 0:
            stdout.write("Yes\n")
        else:
            stdout.write("No\n")


if __name__ == "__main__":
    main()

