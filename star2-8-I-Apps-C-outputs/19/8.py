
import sys
def find_word_ladder(words):
    start, end = words[0], words[1]
    min_steps = -1
    min_word = ""
    for word in words[2:]:
        steps = 0
        for i in range(len(start)):
            if word[i] != start[i]:
                steps += 1
        if steps == 1:
            for j in range(len(end)):
                if word[j] != end[j]:
                    steps += 1
        if steps == 2:
            if min_steps == -1 or steps < min_steps:
                min_steps = steps
                min_word = word
    if min_steps == -1:
        min_word = "0"
        min_steps = -1
    return min_word, min_steps
if __name__ == "__main__":
    num_words = int(sys.stdin.readline().strip())
    words = []
    for _ in range(num_words):
        words.append(sys.stdin.readline().strip())
    min_word, min_steps = find_word_ladder(words)
    print(min_word)
    print(min_steps)

