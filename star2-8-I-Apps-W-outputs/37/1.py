
n,h=map(int,input().split())
l=list(map(int,input().split()))
print(sum(2 if i>h else 1 for i in l))

