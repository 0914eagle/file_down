
def merge_words(words):
    result = words[0]
    for i in range(1, len(words)):
        merged = words[i]
        for j in range(min(len(result), len(merged)), 0, -1):
            if result[-j:] == merged[:j]:
                merged = result + merged[j:]
                break
        result = merged
    return result

n = int(input())
words = input().split()
print(merge_words(words))
