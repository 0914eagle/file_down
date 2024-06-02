
def merge_words(n, words):
    result = words[0]
    for i in range(1, n):
        result = merge_two_words(result, words[i])
    return result

def merge_two_words(word1, word2):
    for i in range(len(word2), 0, -1):
        if word1.endswith(word2[:i]):
            return word1 + word2[i:]
    return word1 + word2

n = int(input())
words = input().split()

compressed_word = merge_words(n, words)
print(compressed_word)
