

h,m,s,t1,t2 = map(int,input().split())

if abs(t1-t2) in [1,11]:
    print("YES")
else:
    print("NO")

