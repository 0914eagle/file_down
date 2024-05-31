
def entirely_unsorted_sequences(n, arr):
    MOD = 10**9 + 9
    factorial = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD
    
    cnt = {}
    for num in arr:
        cnt[num] = cnt.get(num, 0) + 1
    
    result = factorial[n]
    for key in cnt:
        result = (result * pow(factorial[cnt[key]], MOD - 2, MOD)) % MOD
    
    return (result - 1) % MOD

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(entirely_unsorted_sequences(n, arr))
