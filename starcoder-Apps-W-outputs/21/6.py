

def nCr(n,r):
    if n < r:
        return 0
    f = 1
    for i in range(1, r + 1):
        f *= (n + 1 - i)
        f //= i
    return f

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0

    for i in range(m, 1, -1):
        temp = 0
        for j in range(n):
            temp += nCr(i - 1, a[j] - 1)
            temp %= mod
        ans += temp
        ans %= mod

    print(ans)

if __name__ == '__main__':
    mod = 10**9 + 7
    main()

