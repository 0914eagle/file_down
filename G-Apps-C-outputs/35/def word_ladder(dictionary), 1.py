
from collections import deque

def word_ladder(dictionary):
    start_word = dictionary[0]
    end_word = dictionary[1]
    dictionary_set = set(dictionary)
    if end_word not in dictionary_set:
        return "0\n-1"

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    queue = deque([(start_word, 1)])
    while queue:
        word, steps = queue.popleft()
        if word == end_word:
            return "0\n0"
        for i in range(len(word)):
            for letter in alphabet:
                new_word = word[:i] + letter + word[i+1:]
                if new_word in dictionary_set:
                    queue.append((new_word, steps + 1))

    min_steps = float('inf')
    solution_word = ''
    for word in dictionary_set:
        for i in range(len(word)):
            for letter in alphabet:
                new_word = word[:i] + letter + word[i+1:]
                if new_word == end_word:
                    if min_steps > 1:
                        min_steps = 1
                        solution_word = word
                    elif min_steps == 1:
                        solution_word = min(solution_word, word)

    if min_steps == float('inf'):
        return "0\n-1"
    return solution_word + "\n" + str(min_steps)

# Read input
n = int(input())
words = [input().strip() for _ in range(n)]

# Call the function and print the result
print(word_ladder(words))
