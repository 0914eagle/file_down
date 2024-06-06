
for _ in range(int(input())):
    n,k=map(int,input().split())
    list1=[0]*200001
    for i in range(n):
        a,b=map(int,input().split())
        list1[a]+=1
        list1[b+1]-=1
    for i in range(200001):
        if i==0:
            continue
        else:
            list1[i]=list1[i-1]+list1[i]
    count=0
    for i in range(200001):
        if list1[i]>=k:
            count+=1
    a,b=map(int,input().split())
    print(count-(b-a+1))
