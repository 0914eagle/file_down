
def count_complementary_substrings(N, S):
    def check_complementary(T):
        complementary_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        T_permutations = set()
        for i in range(len(T)):
            permuted_T = ''.join(complementary_dict[c] for c in T[i:])
            T_permutations.add(permuted_T)
        return any(perm in T_permutations for perm in T_permutations)

    count = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if check_complementary(S[i:j]):
                count += 1

    return count

# Input
N, S = map(str, input().split())
N = int(N)
result = count_complementary_substrings(N, S)
print(result)
