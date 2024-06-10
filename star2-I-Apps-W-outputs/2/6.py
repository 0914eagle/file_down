
def solve(m, n, a, b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    res = 0
    while i < m and j < n:
        if a[i] < b[j]:
            res += a[i]
            i += 1
        else:
            res += b[j]
            j += 1
    return res


if __name__ == '__main__':
    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(m, n, a, b))

