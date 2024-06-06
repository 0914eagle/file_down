
w,s,c,k = map(int,input().split())
if w+s+c<=k:
    print("YES")
elif w+s<=k and s+c<=k:
    print("YES")
elif s+c<=k and c+w<=k:
    print("YES")
elif w+c<=k and w+s<=k:
    print("YES")
else:
    print("NO")
