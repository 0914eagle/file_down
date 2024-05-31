
MOD = 10**9 + 9

def entirely_unsorted_sequences(n, sequence):
    sorted_count = [0] * n
    total_unsorted = 1
    
    for i in range(n):
        for j in range(i):
            if sequence[j] < sequence[i]:
                sorted_count[i] += 1
        total_unsorted = (total_unsorted * (i + 1 - sorted_count[i])) % MOD
    
    return total_unsorted

# Read input
n = int(input())
sequence = list(map(int, input().split()))

# Calculate and print the result
result = entirely_unsorted_sequences(n, sequence)
print(result)
