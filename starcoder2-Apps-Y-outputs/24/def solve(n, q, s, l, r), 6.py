
def solve(n, q, s, l, r):
    # Write your code here
    return

n, q = map(int, input().split())
s = input()
l = [0] * q
r = [0] * q
for i in range(q):
    l[i], r[i] = map(int, input().split())

ans = solve(n, q, s, l, r)
for i in range(q):
    print(ans[i])

