
# cook your dish here
n,p=map(int,input().split())

apples=1
for i in range(n):
    a=input()
    if a=='halfplus':
        apples+=1
    apples/=2
print(apples*p)
