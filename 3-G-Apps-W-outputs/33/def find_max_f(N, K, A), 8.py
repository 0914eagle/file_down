
def find_max_f(N, K, A):
    max_f = 0
    for i in range(40, -1, -1):
        count = 0
        mask = 1 << i
        new_max_f = max_f | (1 << i)
        for a in A:
            if a & mask:
                count += 1
        if count <= N // 2 and (max_f & mask) == 0 and new_max_f <= K:
            max_f = new_max_f
    return sum(max_f ^ a for a in A)

# Input processing
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Call the function and print the result
print(find_max_f(N, K, A))
