
def count_arrangements(N, M):
    MOD = 10**9 + 7
    
    if abs(N - M) > 1:
        return 0
    
    if N == M:
        return 2 * factorial(N) * factorial(M) % MOD
    else:
        return factorial(N) * factorial(M) % MOD

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = (result * i) % (10**9 + 7)
    return result

N, M = map(int, input().split())
print(count_arrangements(N, M))
