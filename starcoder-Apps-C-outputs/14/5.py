
import re

def haiku(s):
    p=re.compile(r'[A-Za-z]+[A-Za-z\']*')
    l=[0,0,0]
    words=p.findall(s)
    for i in words:
        c=0
        i=i.upper()
        for j in i:
            if j in 'AEIOUY':
                c+=1
        if i[-1]=='E' and i[-2] in 'AEIOUY' and i[-3] in 'BCDFGHJKLMNPQRSTVWXYZ':
            c-=1
        if i[-2:]=='ES' and i[-3] not in 'BCDFGHJKLMNPQRSTVWXYZ':
            c-=1
        l[0]+=c
        if l[0]==5:
            l[1]+=1
            l[0]=0
        if l[1]==2:
            l[2]+=1
            l[1]=0
    if l==[0,0,0]:
        return s
    else:
        return s[:s.index(words[0])]+'\n'+s[s.index(words[0])+len(words[0]):s.index(words[6])]+'\n'+s[s.index(words[6])+len(words[6]):]
s=input()
print(haiku(s))
