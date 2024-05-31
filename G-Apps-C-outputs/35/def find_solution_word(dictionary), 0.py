
from collections import deque

def find_solution_word(dictionary):
    # Helper function to check if two words differ by only one letter
    def is_one_letter_diff(word1, word2):
        diff_count = 0
        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                diff_count += 1
            if diff_count > 1:
                return False
        return diff_count == 1
    
    # Helper function to find all valid words that can be reached from a given word
    def find_valid_words(word, dictionary):
        valid_words = []
        for dict_word in dictionary:
            if is_one_letter_diff(word, dict_word):
                valid_words.append(dict_word)
        return valid_words

    start_word = dictionary[0]
    end_word = dictionary[1]
    dictionary_set = set(dictionary)
    
    queue = deque([(start_word, 1)])  # Initialize queue with starting word and step count
    visited = set([start_word])
    
    while queue:
        current_word, steps = queue.popleft()
        if current_word == end_word:
            return "0", -1  # No word needs to be added if the end word is already reachable
        for word in find_valid_words(current_word, dictionary_set):
            if word not in visited:
                if word == end_word:
                    return "0", steps  # No word needs to be added if end word can be reached
                visited.add(word)
                queue.append((word, steps + 1))
    
    # Find the solution word alphabetically to minimize steps
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(start_word)):
        for char in alphabet:
            new_word = start_word[:i] + char + start_word[i+1:]
            if new_word not in dictionary_set and is_one_letter_diff(start_word, new_word) and is_one_letter_diff(new_word, end_word):
                return new_word, steps + 1
    
    return "0", -1  # No solution word found

# Read input
n = int(input())
dictionary = [input().strip() for _ in range(n)]

# Find and output solution
solution_word, steps = find_solution_word(dictionary)
print(solution_word)
print(steps)
