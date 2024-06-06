

from sys import stdin
h,m,s,t1,t2=map(int,stdin.readline().split())
if t1>t2:
    t1,t2=t2,t1
if t1==t2:
    print("NO")
elif h*3600+m*60+s<t1*3600+t2*3600:
    print("NO")
else:
    print("YES")

