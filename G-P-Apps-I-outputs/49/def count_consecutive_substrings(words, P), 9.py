
def count_consecutive_substrings(words, P):
    count = 0
    for word in words:
        if P in word:
            count += 1
    return count

def barbarians_game(N, words, rounds):
    results = []
    for round in rounds:
        if round[0] == 1:
            P = round[1]
            words.append(P)
        elif round[0] == 2:
            S = round[1]
            result = count_consecutive_substrings(words[:S], words[S-1])
            results.append(result)
    
    return results

# Input processing
N = int(input())
words = [input().strip() for _ in range(N)]

Q = int(input())
rounds = []
for _ in range(Q):
    round_type, *args = input().split()
    rounds.append((int(round_type), *args))

# Get the results
results = barbarians_game(N, words, rounds)

# Output the results
for result in results:
    print(result)
```
