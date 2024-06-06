
n,h,m,k = map(int,input().split())

time = []
for i in range(n):
    time.append(list(map(int,input().split())))
# print(time)
ans = []
for t in range(0,m//2):
    check = True
    for i in time:
        if i[0]*60 + i[1] <= t or i[0]*60 + i[1] > h*60 - k + t:
            check = False
    if check:
        ans.append(t)

if len(ans) == 0:
    print(n,0)
    for i in range(1,n+1):
        print(i)
else:
    print(n-len(ans),ans[0])
