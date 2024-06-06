
w,s,c,k = map(int,input().split())
if w>k or s>k or c>k:
    print("NO")
elif w+s>k or s+c>k:
    print("NO")
else:
    print("YES")
