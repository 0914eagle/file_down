
def solve(s):
    a = 0
    b = 0
    c = 0
    for i in s:
        if i == 'a':
            a += 1
        else:
            b += 1
    if a == b:
        return 0, s
    else:
        if a > b:
            c = a - b
            for i in range(c):
                s = s[:i+1] + 'b' + s[i+1:]
        else:
            c = b - a
            for i in range(c):
                s = s[:i+1] + 'a' + s[i+1:]
        return c, s


def main():
    n = int(input())
    s = input()
    c, s = solve(s)
    print(c)
    print(s)


if __name__ == "__main__":
    main()

