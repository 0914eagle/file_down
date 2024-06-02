
def solve(n, k):
    if n == 3:
        if k == 1:
            return 'abb'
        else:
            return 'bab'
    else:
        if k <= n - 2:
            return 'a' * k + 'b' * (n - k)
        else:
            k -= n - 2
            return 'a' * (n - 2) + 'b' * 2 + solve(n - 2, k)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))

