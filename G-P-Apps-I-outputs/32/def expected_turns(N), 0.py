
def expected_turns(N):
    total_cards = 2 * N
    unknown_cards = total_cards
    matched_pairs = 0
    turns = 0

    while matched_pairs < N:
        if unknown_cards >= 2:
            unknown_cards -= 2
            matched_pairs += 1
        else:
            turns += 1
            unknown_cards += 1

    return turns

N = int(input())
expected_turns = expected_turns(N)
print("{:.9f}".format(expected_turns))
```
