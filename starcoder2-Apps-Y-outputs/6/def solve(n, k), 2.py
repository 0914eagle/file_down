
def solve(n, k):
    s = ['a'] * n
    s[n - 1] = 'b'
    s[n - 2] = 'b'
    k -= 1
    for i in range(n - 3, -1, -1):
        if k >= 2 * i + 1:
            s[i] = 'b'
            k -= 2 * i + 1
        else:
            s[i] = 'a'
    return ''.join(s)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))

