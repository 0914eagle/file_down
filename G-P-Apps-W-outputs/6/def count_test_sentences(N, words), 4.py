
def count_test_sentences(N, words):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    words_set = set(words)
    possible_sentences = []
    
    def find_sentences(current_sentence, remaining_words):
        if len(current_sentence) == 26:
            possible_sentences.append(current_sentence)
            return
        
        for word in remaining_words:
            next_sentence = current_sentence + word
            next_remaining = remaining_words.difference({word})
            if alphabet.issubset(next_sentence):
                find_sentences(next_sentence, next_remaining)
    
    find_sentences('', words_set)
    return len(possible_sentences)

# Read input from user
N = int(input())
words = [input() for _ in range(N)]

# Call the function and print the output
print(count_test_sentences(N, words))
```
