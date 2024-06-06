
from sys import stdin,stdout
from math import factorial
from itertools import combinations
N,D,C=map(int,stdin.readline().split())
Cesar=list(map(int,stdin.readline().split()))
Raul=list(map(int,stdin.readline().split()))

if C>D:
    print(0)
    exit()

if len(set(Cesar).intersection(set(Raul)))>0:
    print(0)
    exit()

prob_C=0
prob_R=0

for i in combinations(range(1,N+1),D):
    if len(set(i).intersection(set(Cesar)))==C:
        prob_C+=1
    if len(set(i).intersection(set(Raul)))==C:
        prob_R+=1

prob_C/=factorial(N)/(factorial(D)*factorial(N-D))
prob_R/=factorial(N)/(factorial(D)*factorial(N-D))

def nCr(n,r):
    f=factorial
    return f(n)/(f(r)*f(n-r))

ans=0
for i in range(C,D+1):
    ans+=nCr(D,i)*((prob_C**i)*((1-prob_C)**(D-i)))

for i in range(C,D+1):
    ans+=nCr(D,i)*((prob_R**i)*((1-prob_R)**(D-i)))

stdout.write(str(ans))
