
def expected_turns(N):
    total_cards = 2 * N
    unmatched_pairs = N
    expected_turns = 0

    while unmatched_pairs > 0:
        prob_new_pair = unmatched_pairs / total_cards
        expected_turns += prob_new_pair

        prob_matching_pair = (total_cards - unmatched_pairs - 1) / total_cards * unmatched_pairs / (total_cards - 1)
        expected_turns += prob_matching_pair

        prob_non_matching_pair = (total_cards - unmatched_pairs - 1) / total_cards * (total_cards - unmatched_pairs - 2) / (total_cards - 1)
        expected_turns += 1 + prob_non_matching_pair

        unmatched_pairs -= 1

    return expected_turns

N = int(input())
print("{:.9f}".format(expected_turns(N)))
```
