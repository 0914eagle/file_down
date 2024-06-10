
import re

def solve(words, queries):
    pattern = re.compile(r"(?=(" + "|".join(words) + "))")
    for query in queries:
        if query[0] == 1:
            words.append(query[1])
        else:
            count = 0
            for word in words:
                count += len(pattern.findall(word))
            print(count)

n = int(input())
words = []
for _ in range(n):
    words.append(input())
q = int(input())
queries = []
for _ in range(q):
    queries.append(list(map(str, input().split())))
solve(words, queries)

