
def count_consecutive_substrings(words, target_word):
    count = 0
    for i in range(len(words) - len(target_word) + 1):
        if words[i:i + len(target_word)] == target_word:
            count += 1
    return count

def barbarians_game(N, barbarians_words, Q, rounds):
    barbarians_dict = {i+1: word for i, word in enumerate(barbarians_words)}

    words_shown = ""
    for round_type, param in rounds:
        if round_type == 1:
            words_shown += param
        elif round_type == 2:
            barbarian_label = param
            target_word = barbarians_dict[barbarian_label]
            count = count_consecutive_substrings(words_shown, target_word)
            print(count)

# Input parsing
N = int(input())
barbarians_words = [input() for _ in range(N)]
Q = int(input())
rounds = [list(map(str, input().split())) for _ in range(Q)]

barbarians_game(N, barbarians_words, Q, rounds)
```
