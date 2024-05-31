
def probability_of_self_gifts(N):
    if N == 1:
        return 0.0
    else:
        total_permutations = 1
        invalid_permutations = 0
        for i in range(2, N+1):
            total_permutations *= i
            if i % 2 == 0:
                invalid_permutations += total_permutations // i
            else:
                invalid_permutations += total_permutations // i

        probability = invalid_permutations / total_permutations
        return round(probability, 8)

# Input
N = int(input())

# Output
print(probability_of_self_gifts(N))
