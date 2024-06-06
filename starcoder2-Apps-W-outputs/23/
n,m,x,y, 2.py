
n,m,x,y=map(int,input().split())
s=input()
a=[[0 for i in range(m+1)]for j in range(n+1)]
a[x][y]=1
for i in range(len(s)):
    if s[i]=='L':
        if y>1:
            y-=1
            a[x][y]=1
    elif s[i]=='R':
        if y<m:
            y+=1
            a[x][y]=1
    elif s[i]=='U':
        if x>1:
            x-=1
            a[x][y]=1
    elif s[i]=='D':
        if x<n:
            x+=1
            a[x][y]=1
ans=[0 for i in range(len(s)+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][j]==1:
            ans[0]+=1
        else:
            ans[len(s)]+=1
for i in range(len(s)):
    for j in range(1,n+1):
        for k in range(1,m+1):
            if a[j][k]==0:
                if j>1 and a[j-1][k]==1:
                    a[j][k]=1
                    ans[i+1]+=1
                elif j<n and a[j+1][k]==1:
                    a[j][k]=1
                    ans[i+1]+=1
                elif k>1 and a[j][k-1]==1:
                    a[j][k]=1
                    ans[i+1]+=1
                elif k<m and a[j][k+1]==1:
                    a[j][k]=1
                    ans[i+1]+=1
for i in range(len(s)+1):
    print(ans[i],end=' ')
