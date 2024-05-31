
from collections import deque

def word_ladder(dictionary):
    start, end = dictionary[0], dictionary[1]
    words = set(dictionary)
    queue = deque([(start, 1)])

    while queue:
        word, steps = queue.popleft()

        if word == end:
            return 0, steps

        for i in range(len(word)):
            for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                next_word = word[:i] + c + word[i+1:]
                if next_word in words:
                    queue.append((next_word, steps + 1))
                    words.remove(next_word)

    min_steps = float('inf')
    solution_word = None

    for word in words:
        queue = deque([(word, 1)])
        found = False

        while queue:
            new_word, steps = queue.popleft()

            if new_word == end:
                if steps < min_steps:
                    min_steps = steps
                    solution_word = word
                found = True
                break

            for i in range(len(new_word)):
                for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    next_word = new_word[:i] + c + new_word[i+1:]
                    if next_word in words:
                        queue.append((next_word, steps + 1))

        if found:
            words.remove(word)

    if solution_word:
        return solution_word, min_steps
    else:
        return 0, -1

# Read input
n = int(input())
dictionary = [input().strip() for _ in range(n)]

# Call the function and print the output
solution_word, min_steps = word_ladder(dictionary)
print(solution_word)
print(min_steps)
