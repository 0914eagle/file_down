
n=int(input())
s=input()
c=m=y=0
for i in range(n):
    if s[i]=='C':
        c=1
    if s[i]=='M':
        m=1
    if s[i]=='Y':
        y=1
if c==1 and m==1 and y==1:
    print('No')
else:
    print('Yes')
