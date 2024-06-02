
def solve(n, k):
    k -= 1
    a = n - 2
    b = 2
    ans = ''
    while a > 0 or b > 0:
        if a > 0 and k >= b:
            ans += 'a'
            k -= b
            a -= 1
        else:
            ans += 'b'
            b -= 1
    return ans

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))

