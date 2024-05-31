
def longest_common_prefix(word1, word2):
    common_prefix = ""
    min_len = min(len(word1), len(word2))
    for i in range(min_len):
        if word1[i] == word2[i]:
            common_prefix += word1[i]
        else:
            break
    return common_prefix

def calculate_steps(database, query_word):
    steps = 0
    for word in database:
        prefix = longest_common_prefix(word, query_word)
        steps += len(prefix) + 1
    return steps

# Input
N = int(input())
database = [input().strip() for _ in range(N)]
Q = int(input())
query_words = [input().strip() for _ in range(Q)]

# Calculate steps for each query word
for query_word in query_words:
    steps = calculate_steps(database, query_word)
    print(steps)
