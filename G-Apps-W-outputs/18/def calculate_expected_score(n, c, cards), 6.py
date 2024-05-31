
import itertools

def calculate_expected_score(n, c, cards):
    total_permutations = list(itertools.permutations(cards, n))
    
    expected_score = 0
    for permutation in total_permutations:
        final_score = -1
        for i in range(c, n):
            if all(permutation[j] <= permutation[i] for j in range(c, i)):
                final_score = permutation[i]
                break
        if final_score == -1:
            final_score = permutation[-1]
        expected_score += final_score
    
    return expected_score / len(total_permutations)

# Input
n, c = map(int, input().split())
cards = list(map(int, input().split()))

# Output
print("{:.6f}".format(calculate_expected_score(n, c, cards)))
