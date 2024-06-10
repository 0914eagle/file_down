
def solve(n, a, b):
    pos = [0] * (n + 1)
    for i in range(n):
        pos[a[i]] = i
    res = 0
    for i in range(n):
        if b[i] == 0:
            continue
        j = pos[b[i]]
        res += j - i
        for k in range(j, i, -1):
            b[k] = b[k - 1]
        b[i] = b[j]
        b[j] = 0
    return res


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, a, b))


