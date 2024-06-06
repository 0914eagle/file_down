
n,l,r = map(int,input().split())
count = 0
for i in range(l-1,r):
    if bin(n>>i & 1)[-1] == '1':
        count +=1
print(count)
