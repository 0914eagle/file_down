
w,s,c,k=map(int,input().split())
if w==0 or s==0 or c==0:
    print("YES")
elif w>k or s>k or c>k:
    print("NO")
elif w+s<=k and c<=k:
    print("YES")
else:
    print("NO")
