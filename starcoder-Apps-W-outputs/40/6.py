
'''input
5
CY??Y
'''
n=int(input())
s=input()
a=s.count('C')
b=s.count('Y')
c=s.count('M')
if s[0]!=s[-1]:
    if s[0]=='?':
        if s[1]=='?':
            if s[-1]=='C':
                a+=1
            elif s[-1]=='Y':
                b+=1
            else:
                c+=1
        elif s[1]=='C':
            if s[-1]=='Y':
                b+=1
            else:
                c+=1
        else:
            if s[-1]=='C':
                a+=1
            else:
                b+=1
    elif s[0]=='C':
        if s[1]=='?':
            if s[-1]=='Y':
                b+=1
            else:
                c+=1
        else:
            if s[-1]=='Y':
                b+=1
            else:
                c+=1
    else:
        if s[1]=='?':
            if s[-1]=='C':
                a+=1
            else:
                b+=1
        else:
            if s[-1]=='C':
                a+=1
            else:
                b+=1
    if a>=2 and b>=2 and c>=2:
        print('Yes')
    else:
        print('No')
else:
    print('No')

