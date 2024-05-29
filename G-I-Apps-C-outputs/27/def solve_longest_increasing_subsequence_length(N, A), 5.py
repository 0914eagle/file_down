
from fractions import Fraction

def solve_longest_increasing_subsequence_length(N, A):
    mod = 1000000007
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    def dp(lst, idx):
        ans = 0
        for i in range(1, A[idx] + 1):
            new_lst = lst[:]
            new_lst.append(i)
            if all(x <= i for x in new_lst):
                if idx == N - 1:
                    ans += len(new_lst)
                else:
                    ans += dp(new_lst, idx + 1)
        return ans
    
    total = dp([], 0)
    p = Fraction(total, A[0])
    q = A[0] * N
    
    for i in range(1, N):
        q = lcm(q, A[i])
    
    result = pow(int(p * q.denominator % mod), mod - 2, mod) * p.numerator % mod
    
    return result

# Read input
N = int(input())
A = list(map(int, input().split()))

# Call function and print the result
print(solve_longest_increasing_subsequence_length(N, A))
```
