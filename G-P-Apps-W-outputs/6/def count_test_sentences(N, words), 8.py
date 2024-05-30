
def count_test_sentences(N, words):
    def has_all_letters(sentence):
        return all(char in sentence for char in 'abcdefghijklmnopqrstuvwxyz')

    def generate_sentences(words, sentence):
        if len(sentence) == 26:
            if has_all_letters(sentence):
                return 1
            else:
                return 0
        if not words:
            return 0

        count = 0
        for i, word in enumerate(words):
            count += generate_sentences(words[i + 1:], sentence + word)
        return count

    return generate_sentences(words, '')

# Read input
N = int(input())
words = [input() for _ in range(N)]

# Calculate and print the output
print(count_test_sentences(N, words))
```
