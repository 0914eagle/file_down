
def longest_common_prefix(word1, word2):
    i = 0
    while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
        i += 1
    return i

def calculate_steps(database, query_word):
    total_steps = 0
    for word in database:
        common_prefix_len = longest_common_prefix(word, query_word)
        total_steps += len(word) + len(query_word) - 2 * common_prefix_len
    return total_steps

# Read input
N = int(input())
database = [input().strip() for _ in range(N)]
Q = int(input())
query_words = [input().strip() for _ in range(Q)]

# Calculate steps for each query word
for query_word in query_words:
    steps = calculate_steps(database, query_word)
    print(steps)
