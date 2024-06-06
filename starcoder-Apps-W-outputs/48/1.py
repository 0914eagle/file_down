
n=int(input())
lst=list(map(int,input().split()))
lst1=[]
for i in range(1,10):
    if n//lst[i-1]>0:
        c=n//lst[i-1]
        lst1.append(str(i)*c)
if lst1==[]:
    print(-1)
else:
    lst1.sort(reverse=True)
    print(''.join(lst1))
