
from math import factorial
N, C = map(int, input().split())
mod = 1000000007
ans = 0
for i in range(C+1):
    ans += ((-1)**i * factorial(N) // (factorial(i)*factorial(N-2*i))*factorial(N-2*i) // factorial(N-C-2*i) % mod) % mod
print(ans % mod)
