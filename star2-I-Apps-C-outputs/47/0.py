
from bisect import bisect_left
from itertools import accumulate

def solve(words, queries):
    words = [word for word in words if word]
    words.sort()
    words = list(accumulate([len(word) for word in words]))
    for query in queries:
        if query[0] == 1:
            word = query[1]
            idx = bisect_left(words, len(word))
            print(idx)
        else:
            idx = bisect_left(words, query[1])
            print(idx)

n = int(input())
words = []
for _ in range(n):
    words.append(input())
q = int(input())
queries = []
for _ in range(q):
    queries.append(list(map(int, input().split())))
solve(words, queries)

