
from collections import deque

def word_ladder(dictionary):
    start = dictionary[0]
    end = dictionary[1]
    
    words = set(dictionary)
    words.add(start)
    words.add(end)
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    queue = deque([(start, 0)])
    visited = set([start])
    
    while queue:
        current_word, steps = queue.popleft()
        
        if current_word == end:
            return ('', steps)
        
        for i in range(len(current_word)):
            for c in alphabet:
                new_word = current_word[:i] + c + current_word[i+1:]
                if new_word in words and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))
    
    min_steps = float('inf')
    min_word = ''
    
    for word in words:
        if word != start and word != end:
            queue = deque([(word, 0)])
            visited = set([word])
            found = False
            
            while queue:
                current_word, steps = queue.popleft()
                
                if current_word == end:
                    found = True
                    min_steps = min(min_steps, steps)
                    break
                
                for i in range(len(current_word)):
                    for c in alphabet:
                        new_word = current_word[:i] + c + current_word[i+1:]
                        if new_word in words and new_word not in visited:
                            visited.add(new_word)
                            queue.append((new_word, steps + 1))
            
            if found and min_steps == steps:
                if min_word == '' or word < min_word:
                    min_word = word
    
    if min_word == '':
        if min_steps == float('inf'):
            return ('0', -1)
        else:
            return ('0', min_steps)
    else:
        return (min_word, min_steps)

# Read input
n = int(input())
dictionary = [input().strip() for _ in range(n)]

# Call the function and print output
result_word, result_steps = word_ladder(dictionary)
print(result_word)
print(result_steps)
