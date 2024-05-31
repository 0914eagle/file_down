
def count_unsorted_sequences(n, a):
    MOD = 10**9 + 9
    fact = [1]
    inv_fact = [1]
    
    for i in range(1, n+1):
        fact.append((fact[-1] * i) % MOD)
        inv_fact.append(pow(fact[-1], MOD-2, MOD))

    def nCr(n, r):
        return (fact[n] * inv_fact[r] * inv_fact[n-r]) % MOD

    a.sort()
    ans = 0
    for i in range(n):
        ways_left = nCr(i, a[i])
        ways_right = nCr(n-i-1, a[i])
        ans = (ans + ways_left * ways_right) % MOD

    return ans

# Input
n = int(input())
a = list(map(int, input().split()))

# Output
print(count_unsorted_sequences(n, a))
