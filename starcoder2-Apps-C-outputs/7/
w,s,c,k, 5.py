
w,s,c,k=map(int,input().split())
if w+s+c<=k:
    print("YES")
elif w+s<=k and c<=k:
    print("YES")
elif w+c<=k and s<=k:
    print("YES")
elif s+c<=k and w<=k:
    print("YES")
else:
    print("NO")
