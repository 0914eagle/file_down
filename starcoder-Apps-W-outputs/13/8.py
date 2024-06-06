
from collections import defaultdict, Counter
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

n,x,k = map(int,input().split())

a = list(map(int,input().split()))

def cal(y,x):
    if x%y!=0:
        return 0
    else:
        return x//y
        

d = Counter(a)

d_new = defaultdict(int)

for i in d:
    if i%x!=0:
        continue
    else:
        for j in d:
            if j%x!=0:
                continue
            else:
                d_new[(cal(x,i),cal(x,j))] = d[i]*d[j]

ans = 0
for i in range(k+1):
    ans += d_new[(i,k-i)]

print(str(ans))
