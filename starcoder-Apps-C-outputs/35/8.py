
n=int(input())
m=int(input())
l=[]
for i in range(m):
    l.append(list(map(int,input().split())))
count=0
for i in range(m):
    count+=min(l[i][2]-l[i][0]+1,l[i][3]-l[i][1]+1)
print(count)
