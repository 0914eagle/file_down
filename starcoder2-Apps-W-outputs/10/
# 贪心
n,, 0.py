
# 贪心
n,m,k = map(int,input().split())
usb = []
ps2 = []
for i in range(m):
    a,b = input().split()
    if b == 'USB':
        usb.append(int(a))
    else:
        ps2.append(int(a))
usb.sort()
ps2.sort()
ans = 0
cost = 0
for i in range(len(usb)):
    if n > 0:
        n -= 1
        ans += 1
        cost += usb[i]
for i in range(len(ps2)):
    if k > 0:
        k -= 1
        ans += 1
        cost += ps2[i]
print(ans,cost)
