
def longest_common_prefix(word1, word2):
    i = 0
    while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
        i += 1
    return i

def steps_to_find_word(database, query_word):
    steps = 0
    for word in database:
        prefix_length = longest_common_prefix(query_word, word)
        steps += 1 + prefix_length
        if prefix_length < len(word) and prefix_length < len(query_word):
            break
    return steps

# Read input
N = int(input())
database = [input().strip() for _ in range(N)]

Q = int(input())
for _ in range(Q):
    query_word = input().strip()
    result = steps_to_find_word(database, query_word)
    print(result)
