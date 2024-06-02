
def max_xor_sum(N, K, A):
    max_val = 0
    for i in range(40, -1, -1):
        mask = 1 << i
        new_max = max_val | mask
        count = 0
        for a in A:
            if (new_max ^ a) <= K:
                count += 1
        if count >= 2:
            max_val = new_max
    result = sum((max_val ^ a) for a in A)
    return result

# Input processing
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Call the function and print the result
print(max_xor_sum(N, K, A))
