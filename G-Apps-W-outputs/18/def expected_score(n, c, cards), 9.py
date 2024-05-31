
import itertools

def expected_score(n, c, cards):
    max_score = 0
    total_ways = 0

    for subset in itertools.combinations(cards, c):
        max_in_subset = max(subset)
        ways_to_observe_max = n - c
        total_ways += ways_to_observe_max

        if max_in_subset == max(cards):
            max_score += max_in_subset
        else:
            count_greater_than_subset_max = sum(1 for x in cards if x > max_in_subset)
            max_score += max_in_subset + count_greater_than_subset_max / ways_to_observe_max * (max(cards) - max_in_subset)

    return max_score / total_ways

# Input
n, c = map(int, input().split())
cards = list(map(int, input().split()))

# Output
print("{:.6f}".format(expected_score(n, c, cards)))
