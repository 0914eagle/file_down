
from math import factorial
def nCr(n,r):
    return factorial(n)//(factorial(n-r)*factorial(r))

# Input
N, D, C = [int(x) for x in input().split()]
cesar = [int(x) for x in input().split()]
raul = [int(x) for x in input().split()]

# Working
rounds = 0
for i in range(1, D+1):
    comb = nCr(D,i)
    c_rem = set(cesar).difference(set(raul))
    r_rem = set(raul).difference(set(cesar))
    rem = len(c_rem) + len(r_rem)
    rounds += comb * (rem/N)**i * ((N-rem)/N)**(D-i)
    
# Output
print(1/rounds)
