
n,m,k=map(int,input().split())
a=[]
for i in range(m):
    a.append(list(map(str,input().split())))
a.sort(key=lambda x:x[0])
usb=0
ps=0
for i in range(m):
    if a[i][1]=='USB':
        usb+=1
    else:
        ps+=1
    if usb==n and ps==k:
        print(n+k,a[i][0])
        break
