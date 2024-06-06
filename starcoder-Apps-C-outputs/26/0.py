
n=int(input())
s=input()
r=[]
for i in range(n):
    if s[i]=='P':
        r.append(i)
max1=-1
for i in r:
    if i>max1:
        max1=i
r.remove(max1)
min1=n
for i in r:
    if i<min1:
        min1=i
print(max(max1-min1,len(s)-min1))
