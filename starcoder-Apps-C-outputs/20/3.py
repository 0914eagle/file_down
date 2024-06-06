
#实现代码
n=int(input())
count=1
L=[]
for i in range(n):
    L.append(input())
if n==1:
    print(1)
else:
    for i in range(1,n):
        if L[i-1][0]==L[i][0]:
            count+=1
    print(count)
