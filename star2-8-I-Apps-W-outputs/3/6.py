
def solve(n, m, table):
    good = True
    for i in range(n - 1):
        for j in range(m):
            if table[i][j] > table[i + 1][j]:
                good = False
                break
        if not good:
            break
    if good:
        return 0
    ans = 0
    for j in range(m):
        good = True
        for i in range(n - 1):
            if table[i][j] > table[i + 1][j]:
                good = False
                break
        if not good:
            ans += 1
    return ans


def main():
    n, m = map(int, input().split())
    table = [input() for _ in range(n)]
    print(solve(n, m, table))


if __name__ == '__main__':
    main()

