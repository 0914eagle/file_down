
s=input()
a=s.split()
d=len(a)
x=[]
for i in range(d):
    s=''
    p=a[i]
    for j in range(len(p)):
        if p[j] not in s:
            s+=p[j]
    x.append(s)
count=0
for i in x:
    if len(i)==len(set(i)) and len(i)<=12:
        count+=1
if count==d:
    print(' '.join(a))
else:
    print('Impossible')
