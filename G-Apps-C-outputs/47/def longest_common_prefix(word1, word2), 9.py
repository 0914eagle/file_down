
def longest_common_prefix(word1, word2):
    i = 0
    while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
        i += 1
    return i

def calculate_steps(database, query):
    steps = 0
    for word in database:
        prefix_len = longest_common_prefix(word, query)
        steps += 1 + prefix_len
        if prefix_len < len(query):
            break
    return steps

# Read input
N = int(input())
database = [input() for _ in range(N)]

Q = int(input())
queries = [input() for _ in range(Q)]

# Calculate steps for each query
for query in queries:
    steps = calculate_steps(database, query)
    print(steps)
