
def solve(n, k):
    k -= 1
    a = n - 2
    b = 2
    while k > 0:
        if k >= a:
            k -= a
            a -= 1
            b += 1
        else:
            a -= 1
    return 'a' * a + 'b' * b

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))

