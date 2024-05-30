
def consecutive_substring_count(words, rounds):
    words_set = set(words)
    count = 0
    for r in rounds:
        if r[0] == 1:
            words_set.add(r[1])
        else:
            barbarian_word = words[r[1] - 1]
            count = sum(1 for w in words_set if w in barbarian_word)
            print(count)

N = int(input())
words = [input() for _ in range(N)]
Q = int(input())
rounds = [list(map(str, input().split())) for _ in range(Q)]

consecutive_substring_count(words, rounds)
```
