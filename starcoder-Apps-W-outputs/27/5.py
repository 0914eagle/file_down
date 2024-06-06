
n=int(input())
a=set()
for _ in range(n):
    a.add(input())
a=sorted(a)

def check(x,y):
    for i in range(min(len(x),len(y))):
        if x[i]!=y[i]:
            return x[i]<y[i]
    return len(x)<len(y)

for i in range(26):
    if check(a[0],a[1]):
        print(''.join(chr(i+ord('a')) for i in range(26)))
        break
    a=a[::-1]
else:
    print('Impossible')

