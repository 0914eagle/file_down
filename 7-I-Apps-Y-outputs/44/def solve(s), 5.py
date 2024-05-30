
def solve(s):
    a = 0
    b = 0
    for i in s:
        if i == 'a':
            a += 1
        else:
            b += 1
    if a == b:
        return 0, s
    if a > b:
        diff = a - b
        for i in range(diff):
            s = s[:i+1] + 'b' + s[i+1:]
    else:
        diff = b - a
        for i in range(diff):
            s = s[:i+1] + 'a' + s[i+1:]
    return diff, s


def main():
    n = int(input())
    s = input()
    diff, s = solve(s)
    print(diff)
    print(s)


if __name__ == '__main__':
    main()

