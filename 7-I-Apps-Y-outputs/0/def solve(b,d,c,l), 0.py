
def solve(b,d,c,l):
    for i in range(1,l//2+1):
        if b*i+d*i+c*i==l:
            print(i,b-i,c-i)
            print(i,b-i,c)
            print(i,b-i,d-i)
            print(i,b,d-i)
            print(i,c-i,d-i)
            print(b-i,c-i,d-i)
    if l==0:
        print(0,0,0)

