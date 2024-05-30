
def test_sentences_count(N, words):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    valid_sentences = set()
    
    def generate_sentences(current_sentence, remaining_words):
        if not alphabet.difference(current_sentence):
            valid_sentences.add(tuple(sorted(current_sentence)))
        
        for i, word in enumerate(remaining_words):
            new_sentence = current_sentence + word
            new_remaining = remaining_words[:i] + remaining_words[i+1:]
            generate_sentences(new_sentence, new_remaining)
    
    generate_sentences('', words)
    
    return len(valid_sentences)

# Input processing
N = int(input())
words = [input() for _ in range(N)]

# Call the function and print the output
print(test_sentences_count(N, words))
```
