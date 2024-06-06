
for _ in range(int(input())):
    l=list(map(int,input().split()))
    if(len(l)==3):
        a,b=l[1],l[2]
        if a>b:
            a,b=b,a
        if len(l)==3 and (a,b) not in l1:
            l1.append((a,b))
        else:
            print("NO")
    else:
        a,b=l[1],l[2]
        if a>b:
            a,b=b,a
        if (a,b) in l1:
            print("YES")
        else:
            print("NO")
