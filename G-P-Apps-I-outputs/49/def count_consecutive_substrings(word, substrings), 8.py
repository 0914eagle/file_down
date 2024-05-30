
def count_consecutive_substrings(word, substrings):
    count = 0
    for sub in substrings:
        if sub in word:
            count += 1
    return count

def barbarians_game(N, barbarians_words, Q, rounds):
    words_set = set()
    for word in barbarians_words:
        words_set.add(word)
    
    results = []
    for round_type, value in rounds:
        if round_type == 1:
            words_set.add(value)
        elif round_type == 2:
            results.append(count_consecutive_substrings(value, words_set))
    
    return results

# Input reading
N = int(input())
barbarians_words = [input().strip() for _ in range(N)]
Q = int(input())
rounds = [list(map(str, input().strip().split())) for _ in range(Q)]

# Solve the game
answers = barbarians_game(N, barbarians_words, Q, rounds)

# Output the answers
for ans in answers:
    print(ans)
```
