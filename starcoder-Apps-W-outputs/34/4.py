
import re
n=input()

a,b=[],[]
for i in range(int(n)):
    s=raw_input().split()
    if s[1]=='1':
        a.append(s[0])
    else:
        b.append(s[0])
for i in range(len(a)):
    print 'move',a[i],i+1
for i in range(len(b)):
    print 'move',b[i],len(a)+1+i
