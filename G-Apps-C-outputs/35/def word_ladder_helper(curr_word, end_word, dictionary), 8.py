
from collections import deque

def word_ladder_helper(curr_word, end_word, dictionary):
    queue = deque([(curr_word, 1)])
    visited = set([curr_word])

    while queue:
        word, steps = queue.popleft()

        if word == end_word:
            return steps

        for i in range(len(word)):
            for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                new_word = word[:i] + char + word[i+1:]
                if new_word in dictionary and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))

    return -1

def find_word_to_add(n, dictionary):
    start_word = dictionary[0]
    end_word = dictionary[1]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    min_steps = float('inf')
    best_word = None

    for word in dictionary:
        for i in range(len(word)):
            for char in alphabet:
                new_word = word[:i] + char + word[i+1:]
                if new_word not in dictionary:
                    dictionary.append(new_word)
                    steps = word_ladder_helper(start_word, end_word, dictionary)
                    if steps == -1:
                        dictionary.pop()
                    else:
                        if steps < min_steps:
                            min_steps = steps
                            best_word = new_word
                        elif steps == min_steps and (best_word is None or new_word < best_word):
                            best_word = new_word
                        dictionary.pop()

    if best_word:
        return best_word, min_steps
    else:
        return 0, -1

# Input parsing
n = int(input())
dictionary = [input().strip() for _ in range(n)]

# Find the word to add and minimum steps
word_to_add, min_steps = find_word_to_add(n, dictionary)

# Output
print(word_to_add)
print(min_steps)
