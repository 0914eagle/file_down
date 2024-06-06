
def solve():
    n, k = map(int, input().split())
    if k > 26 or k > n:
        print(-1)
        return
    b = 'a' * k
    ans = []
    for i in range(n - k):
        ans.append(b[0])
        b = b[1:] + b[0]
    ans.extend(list(b))
    print("".join(ans))

solve()
