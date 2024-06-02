
def solve(l1,r1,l2,r2):
    if l1==l2:
        return l1+1,l2
    if l1==r2:
        return l1,r2+1
    if l2==r1:
        return l2+1,r1
    if l1<l2:
        return l1,l2
    return r1,r2

for _ in range(int(input())):
    l1,r1,l2,r2=map(int,input().split())
    print(*solve(l1,r1,l2,r2))

