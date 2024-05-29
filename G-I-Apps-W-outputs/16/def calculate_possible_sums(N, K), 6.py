
MOD = 10**9 + 7

def calculate_possible_sums(N, K):
    result = 0
    for i in range(K, N + 2):
        first = (10**100 * i) % MOD
        last = (10**100 * (10**100 + i - 1)) % MOD
        count = (last - first + 1) % MOD
        result = (result + count) % MOD
    return result

if __name__ == "__main__":
    N, K = map(int, input().split())
    result = calculate_possible_sums(N, K)
    print(result)
