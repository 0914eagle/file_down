
import sys,os
# sys.stdin=open('in.txt','r')
# sys.stdout=open('out.txt','w')
if  os.path.exists('in.txt'):
    sys.stdin=open('in.txt','r')
n,r,p=map(int,input().split())
print(min(r,p*n))

