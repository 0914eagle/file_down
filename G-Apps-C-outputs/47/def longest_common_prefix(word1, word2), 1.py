
def longest_common_prefix(word1, word2):
    i = 0
    while i < min(len(word1), len(word2)) and word1[i] == word2[i]:
        i += 1
    return word1[:i]

def calculate_steps(database, query):
    steps = 0
    for word in database:
        prefix = longest_common_prefix(word, query)
        steps += 1 + len(prefix)
        if prefix != query:
            break
    return steps

# Read input
N = int(input())
database = [input() for _ in range(N)]
Q = int(input())
queries = [input() for _ in range(Q)]

# Calculate steps for each query word
for query in queries:
    steps = calculate_steps(database, query)
    print(steps)
