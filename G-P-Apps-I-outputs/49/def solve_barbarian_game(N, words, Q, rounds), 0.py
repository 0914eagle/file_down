
def solve_barbarian_game(N, words, Q, rounds):
    substr_count = {}
    for i in range(1, N+1):
        substr_count[i] = 0

    all_words = set()
    for word in words:
        all_words.add(word)

    for t, arg in rounds:
        if t == 1:
            all_words.add(arg)
        elif t == 2:
            for i in range(1, N+1):
                if words[i-1] in arg:
                    substr_count[i] += 1

    for i in range(1, N+1):
        print(substr_count[i])

# Input parsing
N = int(input())
words = []
for _ in range(N):
    words.append(input().strip())

Q = int(input())
rounds = []
for _ in range(Q):
    t, *args = input().split()
    if t == '1':
        rounds.append((int(t), args[0]))
    elif t == '2':
        rounds.append((int(t), int(args[0]))

# Call the function with input values
solve_barbarian_game(N, words, Q, rounds)
```
