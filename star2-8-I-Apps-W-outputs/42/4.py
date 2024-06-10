
def is_magic(n, d, m):
    s = str(n)
    for i in range(len(s)):
        if i % 2 == 0 and int(s[i]) == d:
            if (i + 1) % m == 0:
                return True
    return False


def solve(a, b, d, m):
    res = 0
    for i in range(a, b + 1):
        if is_magic(i, d, m):
            res = (res + 1) % (10 ** 9 + 7)
    return res


m, d = map(int, input().split())
a = int(input())
b = int(input())
print(solve(a, b, d, m))

