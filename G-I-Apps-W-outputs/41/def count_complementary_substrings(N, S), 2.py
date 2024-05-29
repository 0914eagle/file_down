
def count_complementary_substrings(N, S):
    def is_complementary(c1, c2):
        if (c1 == 'A' and c2 == 'T') or (c1 == 'T' and c2 == 'A'):
            return True
        if (c1 == 'C' and c2 == 'G') or (c1 == 'G' and c2 == 'C'):
            return True
        return False

    def check_permutation(sub):
        counter = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for char in sub:
            counter[char] += 1
        if counter['A'] == counter['T'] and counter['C'] == counter['G']:
            return True
        return False

    count = 0

    for i in range(N):
        for j in range(i+1, N+1):
            sub = S[i:j]
            length = j - i
            if check_permutation(sub):
                if all(is_complementary(sub[k], sub[length-1-k]) for k in range(length//2)):
                    count += 1

    return count

N, S = input().split()
N = int(N)
print(count_complementary_substrings(N, S))
```
