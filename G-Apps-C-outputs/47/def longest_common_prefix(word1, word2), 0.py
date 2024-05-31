
def longest_common_prefix(word1, word2):
    common_prefix = []
    min_length = min(len(word1), len(word2))
    for i in range(min_length):
        if word1[i] == word2[i]:
            common_prefix.append(word1[i])
        else:
            break
    return "".join(common_prefix)

def calculate_steps(database, query_word):
    steps = 0
    for word in database:
        lcp = longest_common_prefix(word, query_word)
        steps += 1 + len(lcp)
        if lcp != query_word[:len(lcp)]:
            break
    return steps

# Input processing
N = int(input())
database = [input() for _ in range(N)]

Q = int(input())
queries = [input() for _ in range(Q)]

# Calculate steps for each query word
for query in queries:
    steps = calculate_steps(database, query)
    print(steps)
