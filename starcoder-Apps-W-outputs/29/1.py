
a=list(map(int,input().split()))
n=a[0]
k=a[1]
b=list(map(int,input().split()))
c=[]
if k<n:
    print("NO")
else:
    print("YES")
    for i in range(0,len(b)):
        c.append([])
        if b[i]==1:
            c[i].append(1)
        else:
            if b[i]%2==0:
                if int(b[i]/2)%2==0:
                    for j in range(0,int(b[i]/2)):
                        c[i].append(1)
                        c[i].append(2)
                else:
                    for j in range(0,int(b[i]/2)-1):
                        c[i].append(1)
                        c[i].append(2)
                    c[i].append(3)
            else:
                if int((b[i]-1)/2)%2==0:
                    for j in range(0,int((b[i]-1)/2)):
                        c[i].append(1)
                        c[i].append(2)
                    c[i].append(3)
                else:
                    for j in range(0,int((b[i]-1)/2)):
                        c[i].append(1)
                        c[i].append(2)
                    c[i].append(3)
                    c[i].append(4)
        print(*c[i])

