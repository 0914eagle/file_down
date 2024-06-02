
def merge_words(words):
    result = words[0]
    for i in range(1, len(words)):
        prefix = 0
        for j in range(min(len(result), len(words[i]))):
            if result[-j:] == words[i][:j]:
                prefix = j
        result += words[i][prefix:]
    return result

n = int(input())
words = input().split()
compressed_word = merge_words(words)
print(compressed_word)
