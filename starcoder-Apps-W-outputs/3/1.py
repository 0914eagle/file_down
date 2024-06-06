
# cook your dish here

for _ in range(int(input())):
    n,k,q=map(int,input().split())
    dict={}
    for i in range(n):
        l,r=map(int,input().split())
        for j in range(l,r+1):
            if j in dict:
                dict[j]+=1
            else:
                dict[j]=1
    for i in range(q):
        a,b=map(int,input().split())
        count=0
        for j in range(a,b+1):
            if dict.get(j,0)>=k:
                count+=1
        print(count)
