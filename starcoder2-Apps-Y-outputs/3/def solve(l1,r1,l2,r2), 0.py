
def solve(l1,r1,l2,r2):
    if l1==l2:
        return l1,l1+1
    if r1==r2:
        return r1,r1-1
    if l1<l2 and r1<r2:
        return r1,l2
    if l1>l2 and r1>r2:
        return l1,r2
    if l1<l2 and r1>r2:
        return r1,l2
    if l1>l2 and r1<r2:
        return l1,r2

q=int(input())
for i in range(q):
    l1,r1,l2,r2=map(int,input().split())
    a,b=solve(l1,r1,l2,r2)
    print(a,b)

