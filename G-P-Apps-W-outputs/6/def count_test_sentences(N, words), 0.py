
def count_test_sentences(N, words):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    word_set = set(words)
    count = 0
    
    def dfs(current_sentence, remaining_words):
        nonlocal count
        if len(current_sentence) == 26:
            count += 1
            return
        
        for word in remaining_words:
            if any(char not in alphabet for char in word):
                continue
            
            new_sentence = current_sentence + word
            new_remaining_words = remaining_words - {word}
            dfs(new_sentence, new_remaining_words)
    
    dfs('', word_set)
    return count

# Input parsing
N = int(input())
words = [input() for _ in range(N)]

# Call the function and output result
result = count_test_sentences(N, words)
print(result)
```
