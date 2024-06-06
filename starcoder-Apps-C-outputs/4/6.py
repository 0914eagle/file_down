
import sys
input=sys.stdin.readline
N=int(input())
A=[0]*2*N
B=[0]*2*N

for i in range(N*2):
    c,a=input().split()
    A[i]=int(a)
    if c=='B':
        B[i]=int(a)
    else:
        B[i]=-int(a)

A.sort()
B.sort()

ans=0
for i in range(N*2):
    ans+=abs(A[i]-B[i])

print(ans)
