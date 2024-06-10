
from bisect import bisect_left
from collections import defaultdict

def solve(words, queries):
    n = len(words)
    words = [word for i, word in sorted(words)]
    table = defaultdict(list)
    for i, word in enumerate(words):
        for j in range(len(word)):
            table[word[j]].append(i)
    for t, s in queries:
        if t == 1:
            for c in s:
                table[c].append(n)
            n += 1
        else:
            res = 0
            for c in words[s - 1]:
                i = bisect_left(table[c], s - 1)
                if i < len(table[c]) and table[c][i] == s - 1:
                    res += 1
            print(res)

n = int(input())
words = [input() for _ in range(n)]
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]
solve(words, queries)

