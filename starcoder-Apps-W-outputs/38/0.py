
'''input
11
10
'''

# -*- coding: utf-8 -*-


import numpy as np

def operation(s):
    if len(s)<=1:
        return True
    
    for i in range(len(s)-1):
        if (int(s[i])^int(s[i+1]))==0:
            if (int(s[i])|int(s[i+1]))==1:
                s[i]='1'
                s[i+1]='0'
            elif (int(s[i])|int(s[i+1]))==0:
                s[i]='0'
                s[i+1]='1'
        if operation(s):
            return True
    return False

s1=list(input())
s2=list(input())

if s1==s2:
    print('YES')
else:
    if operation(s1):
        if s1==s2:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

