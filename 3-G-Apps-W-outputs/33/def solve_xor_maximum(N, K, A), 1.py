
def solve_xor_maximum(N, K, A):
    ans = 0
    for i in range(40, -1, -1):
        count = 0
        mask = 1 << i
        new_ans = ans | (1 << i)
        for a in A:
            if a & mask:
                count += 1
        if count <= N // 2 and new_ans <= K:
            ans = new_ans
    f_max = 0
    for a in A:
        f_max += ans ^ a
    return f_max

# Input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Output
print(solve_xor_maximum(N, K, A))
