
def solve(table):
    n = len(table)
    m = len(table[0])
    res = 0
    for j in range(m):
        s = [row[j] for row in table]
        if sorted(s) == s:
            continue
        res += 1
    return res


def main():
    n, m = map(int, input().split())
    table = [input() for i in range(n)]
    res = solve(table)
    print(res)


if __name__ == '__main__':
    main()

