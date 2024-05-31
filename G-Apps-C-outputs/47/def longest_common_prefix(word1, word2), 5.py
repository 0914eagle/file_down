
def longest_common_prefix(word1, word2):
    i = 0
    while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
        i += 1
    return i

def steps_to_find_word(database, query_word):
    steps = 0
    for word in database:
        prefix_length = longest_common_prefix(word, query_word)
        steps += 1 + prefix_length
        if prefix_length < len(query_word):
            break
    return steps

# Input processing
N = int(input())
database = [input().strip() for _ in range(N)]
Q = int(input())
queries = [input().strip() for _ in range(Q)]

# Calculate steps for each query word
for query_word in queries:
    print(steps_to_find_word(database, query_word))
