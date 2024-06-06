
h,m,s,t1,t2=map(int,input().split())
if t1>t2:t2+=12
if t1<h or t2>h:print("NO")
elif t1==h and s==0:print("YES")
else:print("NO")
