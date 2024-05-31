
from collections import deque

def word_ladder(dictionary):
    start = dictionary[0]
    end = dictionary[1]
    words = set(dictionary)
    queue = deque([(start, 1)])
    
    while queue:
        current, steps = queue.popleft()
        if current == end:
            return "0\n-1"  # No word can be added to make the path shorter
        
        for i in range(len(current)):
            for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                new_word = current[:i] + c + current[i+1:]
                if new_word in words:
                    words.remove(new_word)
                    queue.append((new_word, steps + 1))
    
    min_steps = float('inf')
    best_word = None
    for word in words:
        if abs(len(end) - len(word)) <= 1 and len(set(word).symmetric_difference(set(end))) == 1:
            if len(word) == len(end):
                return f"{word}\n{steps + 1}"
            elif len(word) == len(end) + 1:
                min_steps = min(min_steps, steps + 2)
                if not best_word or word < best_word:
                    best_word = word
            elif len(word) == len(end) - 1:
                min_steps = min(min_steps, steps)
                if not best_word or word < best_word:
                    best_word = word
    
    if best_word:
        return f"{best_word}\n{min_steps}"
    else:
        return "0\n0"

# Read input
n = int(input())
dictionary = [input().strip() for _ in range(n)]

# Call the function and output the result
result = word_ladder(dictionary)
print(result)
