
def count_same_subsequences(S, T):
    N, M = len(S), len(T)
    MOD = 10**9 + 7
    
    # Count occurrences of each element in S
    count_S = {num: 0 for num in set(S)}
    for num in S:
        count_S[num] += 1
    
    # Count total possible subsequences for each element in T
    res = 0
    for num in T:
        if num in count_S:
            res = (res + count_S[num]) % MOD
    
    return res

# Read input
N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

# Call the function and print the result
print(count_same_subsequences(S, T))
