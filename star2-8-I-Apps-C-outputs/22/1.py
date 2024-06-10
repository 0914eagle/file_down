
A=int(input())
B=int(input())
L=int(input())
insecure=0
secure=0
supersecure=0
for x in range(1,L+1):
    for y in range(-A,B+1):
        if (x==1 or y==-A or y==B):
            supersecure+=1
        elif(y==0):
            secure+=1
        else:
            insecure+=1
print(insecure)
print(secure)
print(supersecure)

