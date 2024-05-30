
def consecutive_substrings(words, shown_words):
    answer = []
    for shown_word in shown_words:
        if shown_word[0] == 1:
            word = shown_word[1]
            for i in range(len(words)):
                if words[i] in word:
                    answer.append(1)
                    break
            else:
                answer.append(0)
        elif shown_word[0] == 2:
            barbarian_idx = shown_word[1] - 1
            count = 0
            for i in range(len(shown_words[:shown_word[1] - 1])):
                if words[barbarian_idx] in shown_words[i][1]:
                    count += 1
            answer.append(count)
    return answer

# Input
N = int(input())
words = [input() for _ in range(N)]
Q = int(input())
shown_words = [list(map(str, input().split())) for _ in range(Q)]

# Output
for result in consecutive_substrings(words, shown_words):
    print(result)
```
