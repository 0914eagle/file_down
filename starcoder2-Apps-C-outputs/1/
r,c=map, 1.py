
r,c=map(int,input().split())
s=[input() for _ in range(r)]
t=[input() for _ in range(r)]
for i in range(r):
    for j in range(c):
        if s[i][j]!=t[i][j]:
            for k in range(r):
                s[k]=s[k][:j]+'X'+'O'*(c-j-1)
            for k in range(c):
                s[i]=s[i][:k]+'X'+'O'*(r-k-1)
            break
print(1 if s==t else 0)
