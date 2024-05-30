
import numpy as np

def expected_number_of_turns(N):
    total_cards = 2 * N
    seen_cards = set()
    remaining_pairs = N
    expected_turns = 0
    
    while remaining_pairs > 0:
        if len(seen_cards) < N * 2:
            random_card = np.random.randint(1, total_cards + 1)
            if random_card not in seen_cards:
                if len(seen_cards) % 2 == 1:
                    if random_card in seen_cards:
                        seen_cards.remove(random_card)
                        remaining_pairs -= 1
                    else:
                        seen_cards.add(random_card)
                else:
                    seen_cards.add(random_card)
        else:
            random_card1, random_card2 = np.random.choice(list(seen_cards), size=2, replace=False)
            expected_turns += 1
            if random_card1 == random_card2:
                seen_cards.remove(random_card1)
                seen_cards.remove(random_card2)
                remaining_pairs -= 1
        
        expected_turns += 1
    
    return expected_turns

N = 1
expected_turns = expected_number_of_turns(N)
print("{:.9f}".format(expected_turns))
```
