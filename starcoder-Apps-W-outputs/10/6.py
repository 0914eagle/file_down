
a = list(map(int,input().split()))
a.sort()
if a[0]+a[1]+a[2]==a[3]+a[4]+a[5]:
    print("YES")
else:
    print("NO")
