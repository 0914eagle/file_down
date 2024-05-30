
def expected_turns_to_finish_game(N):
    total_cards = 2 * N
    prob_seen = 0
    expected_turns = 0

    for i in range(1, total_cards):
        prob_seen += 2 / (total_cards - i)
        expected_turns += prob_seen

    return expected_turns

N = int(input())
result = expected_turns_to_finish_game(N)
print("{:.9f}".format(result))
```
