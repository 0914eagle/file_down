
def frog(a,b,k):
    if k%2==0:
        return a*k-b*(k/2)
    else:
        return a*(k+1)-b*((k+1)/2)
t=int(input())
for i in range(t):
    a,b,k=map(int,input().split())
    print(frog(a,b,k))
