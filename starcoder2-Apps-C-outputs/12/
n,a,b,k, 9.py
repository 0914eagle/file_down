
n,a,b,k=map(int,input().split())
s=input()
if s=="+":
    print(a**n*b**0%1000000009)
else:
    print((a**n*b**0-a**(n-1)*b**1)%1000000009)
