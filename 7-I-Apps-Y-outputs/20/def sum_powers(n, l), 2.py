
def sum_powers(n, l):
    res = 0
    for i in range(len(l)):
        res += l[i] ** n[i]
    return res


def main():
    n = int(input())
    l = [int(input()) for i in range(n)]
    print(sum_powers(l, range(1, n + 1)))


if __name__ == '__main__':
    main()

