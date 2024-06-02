
def merge_words(word1, word2):
    for i in range(len(word2), 0, -1):
        if word1.endswith(word2[:i]):
            return word1 + word2[i:]
    return word1 + word2

def compress_sentence(n, words):
    compressed_word = words[0]
    for i in range(1, n):
        compressed_word = merge_words(compressed_word, words[i])
    return compressed_word

n = int(input())
words = input().split()

result = compress_sentence(n, words)
print(result)
