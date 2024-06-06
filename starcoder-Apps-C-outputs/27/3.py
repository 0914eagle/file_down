
#Accepted
n = int(input())
x,y = [],[]
for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
x.sort()
y.sort()
distx = x[len(x)//2]-x[len(x)//2-1]
disty = y[len(y)//2]-y[len(y)//2-1]
d = int(input())
if distx+disty>d:
    print("impossible")
else:
    print(n*d-(distx+disty))
