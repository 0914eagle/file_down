
n = list(map(int,input().split()))
m = int(input())
cost = []
for i in range(m):
    cost.append(list(input().split()))
cost.sort(key=lambda x:x[0])
usb = 0
ps = 0
ans = 0
for i in range(m):
    if cost[i][1] == 'USB':
        usb += 1
        ans += int(cost[i][0])
    else:
        ps += 1
        ans += int(cost[i][0])
    if usb >= n[0] and ps >= n[1]+n[2]:
        break
print(usb+ps,ans)
