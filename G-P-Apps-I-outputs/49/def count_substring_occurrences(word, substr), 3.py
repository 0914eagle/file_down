
def count_substring_occurrences(word, substr):
    count = 0
    for i in range(len(word) - len(substr) + 1):
        if word[i:i + len(substr)] == substr:
            count += 1
    return count

def barbarian_game(N, barbarians, Q, rounds):
    words = {}
    for i in range(N):
        words[i] = barbarians[i]
    
    shown_words = []
    for i in range(Q):
        round_type, *params = rounds[i]
        if round_type == 1:
            shown_words.append(params[0])
        elif round_type == 2:
            barbarian_idx = params[0] - 1
            word = words[barbarian_idx]
            total_count = sum(count_substring_occurrences(shown_word, word) for shown_word in shown_words)
            print(total_count)

# Input parsing
N = int(input())
barbarians = [input().strip() for _ in range(N)]
Q = int(input())
rounds = [list(map(str, input().split())) for _ in range(Q)]

barbarian_game(N, barbarians, Q, rounds)
```
