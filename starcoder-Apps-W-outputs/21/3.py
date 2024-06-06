

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (m + 1)
    b[1] = m - 1
    for i in range(2, m + 1):
        b[i] = b[i - 1] + (m - 1 - i) // 2
    ans = 0
    for i in range(n):
        ans += b[a[i]]
    print(ans)


if __name__ == '__main__':
    main()
