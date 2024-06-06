
k=int(input())
d=list(map(int,input().split()))
d.sort()
print(len(d))
for i in d:
    print(i,end=" ")
