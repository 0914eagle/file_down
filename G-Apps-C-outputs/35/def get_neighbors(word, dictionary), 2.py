
from collections import deque

def get_neighbors(word, dictionary):
    neighbors = []
    for i in range(len(word)):
        for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            new_word = word[:i] + ch + word[i+1:]
            if new_word in dictionary:
                neighbors.append(new_word)
    return neighbors

def word_ladder(dictionary):
    start_word = dictionary[0]
    end_word = dictionary[1]
    
    queue = deque([(start_word, 0)])
    visited = set()
    
    while queue:
        curr_word, steps = queue.popleft()
        visited.add(curr_word)
        
        if curr_word == end_word:
            return "0", -1
        
        for neighbor in get_neighbors(curr_word, dictionary):
            if neighbor not in visited:
                if neighbor == end_word:
                    return "0", steps + 1
                queue.append((neighbor, steps + 1))
    
    min_steps = float('inf')
    solution_word = ""
    
    for word in dictionary:
        if word != start_word and word != end_word:
            if get_neighbors(start_word, dictionary) and get_neighbors(word, dictionary) and get_neighbors(end_word, dictionary):
                steps_start = len(
                    deque([(start_word, 0)]) - len(deque([(word, 0)]) - len(deque([(end_word, 0)])))
                
                if steps_start < min_steps:
                    min_steps = steps_start
                    solution_word = word
                    
    if min_steps == float('inf'):
        return "0", -1
    else:
        return solution_word, min_steps

# Read input
n = int(input())
dictionary = [input().strip() for _ in range(n)]

# Call the function and print output
solution_word, steps = word_ladder(dictionary)
print(solution_word)
print(steps)
