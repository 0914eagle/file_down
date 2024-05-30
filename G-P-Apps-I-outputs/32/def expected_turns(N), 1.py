
def expected_turns(N):
    total_cards = 2 * N
    matched_cards = 0
    turns = 0

    while matched_cards < total_cards:
        if matched_cards == 0:
            turns += 1
            matched_cards += 1
        elif matched_cards % 2 == 0:
            # No pair to match, turn a random unknown card face up
            turns += 1
            matched_cards += 1
        else:
            # Match a pair
            turns += 1
            matched_cards += 2

    return turns

N = int(input())
expected = expected_turns(N)
print("{:.9f}".format(expected))
```
