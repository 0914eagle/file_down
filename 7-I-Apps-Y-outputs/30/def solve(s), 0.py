
def solve(s):
    n = len(s)
    if n % 3 == 0:
        return s
    elif n % 3 == 1:
        if s[0] == '0':
            return '0' + s[1:]
        elif s[0] == '1':
            return '2' + s[1:]
        else:
            return '1' + s[1:]
    else:
        if s[0] == '0':
            return '2' + s[1:]
        elif s[0] == '1':
            return '0' + s[1:]
        else:
            return '1' + s[1:]


def main():
    n = int(input())
    s = input()
    print(solve(s))


if __name__ == "__main__":
    main()

