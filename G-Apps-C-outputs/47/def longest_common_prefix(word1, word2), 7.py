
def longest_common_prefix(word1, word2):
    prefix = ""
    min_len = min(len(word1), len(word2))
    for i in range(min_len):
        if word1[i] == word2[i]:
            prefix += word1[i]
        else:
            break
    return prefix

def calculate_steps(database, query):
    steps = 0
    for word in database:
        prefix = longest_common_prefix(word, query)
        steps += len(prefix) + 1
    return steps

N = int(input())
database = [input().strip() for _ in range(N)]

Q = int(input())
for _ in range(Q):
    query = input().strip()
    steps = calculate_steps(database, query)
    print(steps)

