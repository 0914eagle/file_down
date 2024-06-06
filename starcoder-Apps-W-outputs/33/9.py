
#https://www.geeksforgeeks.org/python-program-check-input-number-prime/
def prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True

n=int(input())
l=[]
for i in range(n):
    l1=[int(x) for x in input().split()]
    l.append(l1)

a=[]
for i in range(n):
    for j in range(1,l[i][0]+1):
        a.append(l[i][j])

b=[]
for i in range(n):
    for j in range(1,l[i][0]+1):
        if(prime(l[i][j])):
            b.append(l[i][j])
if(len(a)==len(b)):
    print("impossible")
else:
    for i in range(n):
        for j in range(1,l[i][0]+1):
            if(prime(l[i][j])):
                print(i+1,j,l[i][j])
