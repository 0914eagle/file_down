
def count_row(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return 1
    return 0


def solve():
    n, m = map(int, input().split())
    count = 0
    for i in range(n):
        s = input()
        count += count_row(s)

    print(count)


solve()

