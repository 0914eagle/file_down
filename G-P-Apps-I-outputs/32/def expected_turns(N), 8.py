
def expected_turns(N):
    total_cards = 2 * N
    expected_turns = 0
    known_cards = set()
    unknown_cards = set(range(total_cards))

    while len(known_cards) < total_cards:
        if len(known_cards) >= 2:
            pair = next(iter(known_cards))
            known_cards.remove(pair)
            known_cards.remove(pair)
            expected_turns += 1
        else:
            if len(known_cards) == 1:
                first_card = next(iter(known_cards))
            else:
                first_card = unknown_cards.pop()
                known_cards.add(first_card)

            second_card = unknown_cards.pop()
            known_cards.add(second_card)
            
            if first_card // 2 == second_card // 2:
                expected_turns += 1
                known_cards.remove(first_card)
                known_cards.remove(second_card)
            else:
                expected_turns += 1

    return expected_turns

N = int(input())
print("{:.9f}".format(expected_turns(N)))
```
