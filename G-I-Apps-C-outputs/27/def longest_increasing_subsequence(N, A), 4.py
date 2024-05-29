
def longest_increasing_subsequence(N, A):
    MOD = 1000000007
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def expected_length():
        ans = 0
        for i in range(1, N + 1):
            numerator = 1
            denominator = 1
            for j in range(1, i):
                numerator = (numerator * (A[j - 1] - j + 1)) % MOD
                denominator = (denominator * j) % MOD
            ans = (ans + numerator * pow(denominator, -1, MOD)) % MOD
        return ans
    
    return expected_length()

N = int(input())
A = list(map(int, input().split()))

print(longest_increasing_subsequence(N, A))
```
