
def solve(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return (n - i - 1) + (n // 2 - i)
    return 0


def main():
    s = input()
    print(solve(s))


if __name__ == "__main__":
    main()

