
a,b,c,d=map(int,input().split())
if a+b+c+d==2:
    print("YES")
    print(0,0,1,1)
elif a+b+c+d==3:
    print("YES")
    print(0,1,2,0)
elif a+b+c+d==4:
    print("YES")
    print(0,1,2,3,0)
elif a+b+c+d==5:
    print("YES")
    print(0,1,2,3,0,1)
elif a+b+c+d==6:
    print("YES")
    print(0,1,2,3,0,1,2)
elif a+b+c+d==7:
    print("YES")
    print(0,1,2,3,0,1,2,3)
elif a+b+c+d==8:
    print("YES")
    print(0,1,2,3,0,1,2,3,0)
elif a+b+c+d==9:
    print("YES")
    print(0,1,2,3,0,1,2,3,0,1)
elif a+b+c+d==10:
    print("YES")
    print(0,1,2,3,0,1,2,3,0,1,2)
else:
    print("NO")
