
from collections import deque

def word_ladder(dictionary):
    def is_adjacent(word1, word2):
        diff = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                diff += 1
            if diff > 1:
                return False
        return diff == 1

    n = len(dictionary)
    start_word, end_word = dictionary[0], dictionary[1]
    if start_word == end_word:
        return "0\n-1"

    dictionary_set = set(dictionary)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    queue = deque([(start_word, 1)])
    added_word = ""

    while queue:
        word, steps = queue.popleft()
        if word == end_word:
            return f"{added_word}\n{steps - 1}"

        for i in range(len(word)):
            for letter in alphabet:
                new_word = word[:i] + letter + word[i+1:]
                if new_word in dictionary_set:
                    queue.append((new_word, steps + 1))
                    dictionary_set.remove(new_word)
                    if len(added_word) == 0:
                        added_word = new_word

    return "0\n-1"

# Reading input
n = int(input())
dictionary = [input().strip() for _ in range(n)]

# Output result
print(word_ladder(dictionary))
