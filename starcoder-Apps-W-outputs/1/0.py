
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=set()
    for i in range(m):
        x,y=map(int,input().split())
        a.add(x+y)
    if m%2==0 and n%2==0:
        print("Yes")
    else:
        print("No")
