
def longest_common_prefix(word1, word2):
    prefix = ""
    for char1, char2 in zip(word1, word2):
        if char1 == char2:
            prefix += char1
        else:
            break
    return prefix

def calculate_steps(database, query_word):
    steps = 0
    for word in database:
        prefix = longest_common_prefix(word, query_word)
        steps += len(prefix) + 1
    return steps

# Input
N = int(input())
database = [input() for _ in range(N)]
Q = int(input())
query_words = [input() for _ in range(Q)]

# Output
for query_word in query_words:
    steps = calculate_steps(database, query_word)
    print(steps)
