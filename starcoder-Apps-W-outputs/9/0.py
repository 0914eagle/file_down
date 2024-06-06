
n,p=map(int,input().split())
x=0
for i in range(n):
    s=input()
    if s[0]=='h':
        x=x+p//2
print(x)
