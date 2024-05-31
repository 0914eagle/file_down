
from collections import deque

def word_ladder(dictionary):
    start_word = dictionary[0]
    end_word = dictionary[1]
    word_length = len(start_word)
    
    if start_word == end_word:
        return "0\n-1"
    
    if word_length == 1:
        return "A\n1"
    
    dictionary_set = set(dictionary)
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    queue = deque([(start_word, 1)])

    while queue:
        current_word, steps = queue.popleft()
        
        if current_word == end_word:
            return "0\n" + str(steps - 1)
        
        for i in range(word_length):
            for letter in alphabet:
                new_word = current_word[:i] + letter + current_word[i + 1:]
                
                if new_word in dictionary_set:
                    queue.append((new_word, steps + 1))
                    dictionary_set.remove(new_word)
    
    return "0\n-1"

# Reading input
n = int(input())
dictionary = [input().strip() for _ in range(n)]

# Output
print(word_ladder(dictionary))
