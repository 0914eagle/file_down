
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
s1 = s2 = 0
for i in range(n):
    if(a[i]>0):
        s1+=a[i]
    else:
        s2+=(-1)*a[i]
if(s1>s2):
    print('first')
elif(s1<s2):
    print('second')
else:
    for i in range(n):
        if(a[i]>0):
            print('first')
            break
        elif(a[i]<0):
            print('second')
            break
