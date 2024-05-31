
def count_unsorted_sequences(n, arr):
    MOD = 10**9 + 9
    
    factorials = [1]
    for i in range(1, n+1):
        factorials.append((factorials[-1] * i) % MOD)
    
    def nCr(n, r):
        return (factorials[n] * pow(factorials[r], MOD-2, MOD) * pow(factorials[n-r], MOD-2, MOD)) % MOD
    
    sorted_counts = {}
    sorted_count = 0
    total_unsorted = 0
    
    for num in arr:
        if num not in sorted_counts:
            sorted_counts[num] = 0
        total_unsorted += n - 1 - sorted_counts[num]
        sorted_count += 1
        sorted_counts[num] = sorted_count
    
    return (factorials[n] - total_unsorted) % MOD

# Input parsing
n = int(input())
arr = list(map(int, input().split()))

result = count_unsorted_sequences(n, arr)
print(result)
