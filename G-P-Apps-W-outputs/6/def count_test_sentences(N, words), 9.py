
def count_test_sentences(N, words):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    total = 0

    def dfs(index, current_sentence):
        nonlocal total

        if len(current_sentence) == 26:
            total += 1
            return

        if index >= N:
            return

        dfs(index + 1, current_sentence)  # Skip current word
        dfs(index + 1, current_sentence + words[index])  # Include current word

    dfs(0, "")

    return total

# Example input
N = 9
words = ["the", "quick", "brown", "fox", "jumps", "over", "a", "sleazy", "dog"]
print(count_test_sentences(N, words))

N = 3
words = ["a", "b", "c"]
print(count_test_sentences(N, words))
```
