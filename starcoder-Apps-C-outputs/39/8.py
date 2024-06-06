
n,g=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
arr.sort(key=lambda x:x[0])
ans=[]
for i in range(n):
    if arr[i][0]<=g:
        ans.append(arr[i])
    else:
        break
ans=ans[::-1]
if ans==[]:
    print('cancel road trip')
else:
    m=min(ans,key=lambda x:x[1])
    print(m[1])
