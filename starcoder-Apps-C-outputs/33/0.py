
def cal(a,b,l,r):
    if a==1:
        return 2
    if r/a<b+1:
        return 1
    if l/a<=b+1:
        return 0
    if a==b:
        return a
    if l/a==r/a:
        return 1
    return 0

if __name__=='__main__':
    a,b,l,r=map(int,raw_input().split())
    print cal(a,b,l,r)
