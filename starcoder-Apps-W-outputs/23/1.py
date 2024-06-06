
import random
n=int(input())
for i in range(n):
    k=int(input())
    m=list(map(int,input().split()))
    j=random.randint(0,k-1)
    print(m[j])
