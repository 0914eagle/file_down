
n=int(input())
l=list(map(int,input().split()))
s=sorted(l)
print(n)
for i in range(n):
    print(l.index(s[i]),i)


