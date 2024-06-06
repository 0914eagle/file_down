
n=int(input())
x,y=[],[]
for i in range(n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
d=int(input())

if min(x)+d>=max(x)-d or min(y)+d>=max(y)-d:
    print('impossible')
else:
    x_=min(x)
    y_=min(y)
    x__=max(x)
    y__=max(y)
    t=0
    for i in range(n):
        t=t+min(abs(x[i]-x_),abs(x[i]-x__))+min(abs(y[i]-y_),abs(y[i]-y__))
    print(t)
