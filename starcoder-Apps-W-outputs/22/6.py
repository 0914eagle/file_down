
s=input()
a=len(s)
k=s.index('^')
sum1=0
for i in range(k-1,-1,-1):
    if s[i]!='=':
        sum1+=int(s[i])
    if i==0:
        break
sum2=0
for i in range(k+1,a,1):
    if s[i]!='=':
        sum2+=int(s[i])
if sum1==sum2:
    print('balance')
elif sum1>sum2:
    print('left')
else:
    print('right')
