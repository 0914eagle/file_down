
s=input()
s=s.split()
n=int(s[0])
a=input()
a=a.split()
for i in range(n):
    a[i]=int(a[i])
for i in range(n-1):
    m=max(a)
    if(m==a[0]):
        a[0]=a[1]+a[n-1]
        a[n-1]=0
    else:
        for i in range(1,n-1):
            if(a[i]==m):
                a[i-1]=a[i]+a[i-1]
                a[i]=0
                a[i+1]=0
                break
        if(a[n-2]==m):
            a[n-2]=0
            a[n-1]=a[n-2]+a[n-1]
print(max(a))

