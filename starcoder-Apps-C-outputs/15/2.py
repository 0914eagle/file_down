
n,c=map(int,input().split())
l=[1]*n
for i in range(c):
    l[i]=0
print(sum(l)%(1000000007))
