

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    s = 'a' * (n - 2) + 'bb'
    k -= 1
    for i in range(n - 2):
        if k >= 2 * (n - 2 - i):
            k -= 2 * (n - 2 - i)
            s = s[:i] + 'b' + s[i:]
    print(s)


