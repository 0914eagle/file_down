
L,R = map(int,input().split())

ans = [0,0,0,0,0,0,0,0,0]
for i in range(L,R+1):
    i = str(i)
    if len(i)==1:
        ans[int(i)-1]+=1
    else:
        while len(i) != 1:
            i = str(eval('*'.join(i)))
        ans[int(i)-1]+=1
print(' '.join(map(str,ans)))
