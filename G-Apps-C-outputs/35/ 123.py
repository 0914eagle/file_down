
from collections import defaultdict, deque

def word_ladder(n, words):
    word_len = len(words[0])
    adj_list = defaultdict(list)
    for word in words:
        for i in range(word_len):
            key = word[:i] + '*' + word[i+1:]
            adj_list[key].append(word)
    
    queue = deque()
    visited = set()
    queue.append((words[0], 1))
    visited.add(words[0])
    
    while queue:
        curr_word, level = queue.popleft()
        for i in range(word_len):
            key = curr_word[:i] + '*' + curr_word[i+1:]
            for word in adj_list[key]:
                if word == words[1]:
                    return "0\n-1"
                if word not in visited:
                    visited.add(word)
                    queue.append((word, level+1))
    
    min_steps = float('inf')
    solution_word = None
    
    for i in range(word_len):
        for word in words:
            for j in range(ord('A'), ord('Z')+1):
                new_word = word[:i] + chr(j) + word[i+1:]
                if new_word in adj_list[word[:i] + '*' + word[i+1:]]:
                    queue.append((new_word, 1))
                    visited.add(new_word)
                    while queue:
                        curr_word, level = queue.popleft()
                        if curr_word == words[1]:
                            if level < min_steps:
                                min_steps = level
                                solution_word = new_word
                            break
                        for k in range(word_len):
                            key = curr_word[:k] + '*' + curr_word[k+1:]
                            for next_word in adj_list[key]:
                                if next_word not in visited:
                                    visited.add(next_word)
                                    queue.append((next_word, level+1))
    
    if solution_word:
        return solution_word + "\n" + str(min_steps)
    return "0\n0"

# Input
n = int(input())
words = [input().strip() for _ in range(n)]

# Output
print(word_ladder(n, words))
