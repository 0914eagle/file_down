
w,s,c,k = map(int,input().split())
if w>k or s>k or c>k:
    print('NO')
else:
    if w+s<=k and c<=k:
        print('YES')
    else:
        print('NO')
