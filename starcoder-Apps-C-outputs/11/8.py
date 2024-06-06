
h,m,s,t1,t2=input().split()
h=int(h)
m=int(m)
s=int(s)
t1=int(t1)
t2=int(t2)

list=[h,m//5,s//5]
if t1 in list or t2 in list or t1==t2:
    print('NO')
else:
    print('YES')
