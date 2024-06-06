
b1,q,l,m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
x = b1
while abs(x) <= l:
    if x not in a:
        ans += 1
    x += q
if ans:
    print(ans)
else:
    print("inf")
