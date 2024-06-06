
r,x1,y1,x2,y2=map(float,input().split())
x0=(x1+x2)/2
y0=(y1+y2)/2
r=((r**2)*(x1-x2)**2+(r**2)*(y1-y2)**2)**0.5/2
print(x0,y0,r)
