
def solve(n, k):
    k -= 1
    a = n - 2
    b = 2
    s = ''
    while a > 0:
        if k >= a:
            s += 'a' * a + 'b' * b
            k -= a
            a = 0
        else:
            s += 'a' * k + 'b' * b
            a -= k
            k = 0
    return s

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))

