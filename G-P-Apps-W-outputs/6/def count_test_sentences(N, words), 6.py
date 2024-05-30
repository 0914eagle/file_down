
def count_test_sentences(N, words):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    total_words = set(words)
    result = 0

    def backtrack(curr_sentence, remaining_words):
        nonlocal result
        if len(curr_sentence) == 26:
            result += 1
            return

        for word in remaining_words:
            new_sentence = curr_sentence + word
            new_remaining = remaining_words - set(word)

            if len(new_sentence) <= 26 and set(new_sentence) | alphabet == alphabet:
                backtrack(new_sentence, new_remaining)

    backtrack('', total_words)
    return result

# Input processing
N = int(input())
words = [input().strip() for _ in range(N)]

# Call the function
output = count_test_sentences(N, words)
print(output)
```
