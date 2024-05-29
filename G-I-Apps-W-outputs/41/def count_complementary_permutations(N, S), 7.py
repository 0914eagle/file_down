
def count_complementary_permutations(N, S):
    def is_complementary(char1, char2):
        if (char1 == 'A' and char2 == 'T') or (char1 == 'T' and char2 == 'A'):
            return True
        if (char1 == 'C' and char2 == 'G') or (char1 == 'G' and char2 == 'C'):
            return True
        return False
    
    def count_permutations(substring):
        counter = {}
        for char in substring:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        return counter
    
    count = 0
    for length in range(1, N + 1):
        for start in range(N - length + 1):
            end = start + length
            substr = S[start:end]
            permutations = set()
            for i in range(length):
                sub_perm = S[start+i:end] + S[start:start+i]
                if is_complementary(sub_perm[i], substr[i]) and count_permutations(sub_perm) == count_permutations(substr):
                    permutations.add(sub_perm)
            if substr in permutations:
                count += 1
    
    return count

# Input
N, S = input().split()
N = int(N)

# Output
print(count_complementary_permutations(N, S))
