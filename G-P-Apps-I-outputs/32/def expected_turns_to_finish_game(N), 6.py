
def expected_turns_to_finish_game(N):
    total_cards = 2 * N
    remaining_pairs = N
    expected_turns = 0

    while remaining_pairs > 0:
        unknown_cards = total_cards - 2 * remaining_pairs
        probability_matching_known = remaining_pairs / unknown_cards
        probability_not_matching_known = 1 - probability_matching_known

        expected_turns += 1
        remaining_pairs -= 1
        expected_turns += probability_not_matching_known * (1 + expected_turns)

    return expected_turns

N = int(input())
result = expected_turns_to_finish_game(N)
print("{:.9f}".format(result))
```
