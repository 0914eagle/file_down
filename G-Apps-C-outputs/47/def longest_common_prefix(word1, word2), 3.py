
def longest_common_prefix(word1, word2):
    i = 0
    while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
        i += 1
    return i

def calculate_steps(database, query):
    steps = 0
    for word in database:
        prefix_length = longest_common_prefix(word, query)
        steps += 1 + prefix_length
        if prefix_length < len(query):
            break
    return steps

N = int(input())
database = [input() for _ in range(N)]

Q = int(input())
for _ in range(Q):
    query = input()
    steps = calculate_steps(database, query)
    print(steps)
