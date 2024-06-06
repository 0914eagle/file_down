
# 纯模拟，一点想法都没有
# 纯模拟，一点想法都没有
# 纯模拟，一点想法都没有
import math
w,h,x,y=map(int,input().split())
g=eval(input())

s=[]
d={}

for i in range(h):
    for j in range(w):
        if i==x and j==y:
            s.append((0,0,0))
            d[0]=0
        else:
            s.append((abs(g[i][j]-g[x][y]),i,j))
            d[abs(g[i][j]-g[x][y])]=min(i,j)

t=1
while t<=12:
    l=[]
    # print(s)
    for i in range(h):
        for j in range(w):
            # print(i,j)
            if s[i*w+j][0]<=0.5*a*(math.cos((t*2*math.pi)/12)+1) and s[i*w+j][0]>=0:
                if i>0:
                    l.append((s[i*w+j][0],s[(i-1)*w+j][1]+1,s[(i-1)*w+j][2]))
                if i<h-1:
                    l.append((s[i*w+j][0],s[(i+1)*w+j][1]+1,s[(i+1)*w+j][2]))
                if j>0:
                    l.append((s[i*w+j][0],s[i*w+j-1][1]+1,s[i*w+j-1][2]))
                if j<w-1:
                    l.append((s[i*w+j][0],s[i*w+j+1][1]+1,s[i*w+j+1][2]))
    for i in l:
        s.append(i)
        d[i[0]]=min(i[1],i[2])
    t+=0.1

print(d[max(d)])
