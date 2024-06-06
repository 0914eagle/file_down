
# cook your dish here

n,k,q = map(int,input().split())
li = []
for i in range(n):
    li.append(list(map(int,input().split())))
s = []
for i in range(q):
    s.append(list(map(int,input().split())))
for i in s:
    c=0
    for j in li:
        if i[0]<=j[0]<=i[1] or i[0]<=j[1]<=i[1]:
            c+=1
    if c>=k:
        print(i[1]-i[0]+1)
    else:
        print(0)
