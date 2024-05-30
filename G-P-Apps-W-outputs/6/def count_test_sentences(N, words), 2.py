
def count_test_sentences(N, words):
    target = set('abcdefghijklmnopqrstuvwxyz')
    result = 0
    
    def backtrack(curr_sentence, used_words):
        nonlocal result
        if set(curr_sentence) == target:
            result += 1
            return
        
        for i, word in enumerate(words):
            if i not in used_words:
                new_sentence = curr_sentence + word
                new_used_words = used_words + [i]
                backtrack(new_sentence, new_used_words)
    
    backtrack('', [])
    return result

# Input parsing
N = int(input())
words = [input().strip() for _ in range(N)]

# Call the function with input values
output = count_test_sentences(N, words)
print(output)
```
