
def entirely_unsorted_sequences(n, arr):
    mod = 10**9 + 9
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % mod
    
    count = [0] * (n + 1)
    for i in range(n):
        less_count = 0
        for j in range(i):
            if arr[j] < arr[i]:
                less_count += 1
        count[i] = (fact[n - i - 1] * less_count) % mod
        
    total = 0
    for i in range(n):
        total = (total + count[i]) % mod
    
    return total

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Call function and print the result
result = entirely_unsorted_sequences(n, arr)
print(result)
