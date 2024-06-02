
def merge_words(words):
    result = words[0]
    for i in range(1, len(words)):
        merged = merge(result, words[i])
        result = merged
    return result

def merge(word1, word2):
    for i in range(len(word2), 0, -1):
        if word1.endswith(word2[:i]):
            return word1 + word2[i:]
    return word1 + word2

n = int(input())
words = input().split()
print(merge_words(words))
