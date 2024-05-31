
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_ways(n, students):
    MOD = 10**9 + 7
    factors = [set() for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            if gcd(students[i], students[j]) != 1:
                factors[i].add(j)
                factors[j].add(i)

    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][(i+1) % n] = 1

    for length in range(2, n):
        for i in range(n):
            j = (i + length) % n
            for k in range((i+1) % n, j):
                if k not in factors[i]:
                    continue
                dp[i][j] += dp[i][k] * dp[k][j]
                dp[i][j] %= MOD

    total_ways = sum(dp[i][(i-1) % n] for i in range(n))
    return total_ways % MOD

# Read input
n = int(input())
students = []
for _ in range(n):
    students.append(int(input()))

# Output the result
print(count_ways(n, students))
