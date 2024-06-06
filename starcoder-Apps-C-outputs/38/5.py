
#in this problem we need to find the sum of x^k where 1≤x≤N and 1≤k≤5000
import math
t=int(input())
n,k=map(int,input().split())
sum=0
for i in range(1,n+1):
    sum=sum+math.pow(i,k)
print(int(sum%(10**9+7)))
