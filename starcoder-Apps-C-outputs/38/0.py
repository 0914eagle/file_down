
import math

n,k = map(int,input().split())

m = 1000000007
if n == 1:
    print(1)
else:
    print(int((pow(n,k+1,m) - n)/n%m))
