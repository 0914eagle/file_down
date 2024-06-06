
x,y,a,b=map(int,input().split())
c=0
for i in range(a,x+1):
    for j in range(b,y+1):
        if i>j:
            c+=1
print(c)
