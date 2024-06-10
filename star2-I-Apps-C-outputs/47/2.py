
from bisect import bisect_left
from collections import defaultdict

def solve(words, queries):
    n = len(words)
    words = [word for word in words if len(word) > 0]
    n = len(words)
    words.sort()
    trie = defaultdict(lambda: defaultdict(int))
    for word in words:
        cur = trie
        for c in word:
            cur = cur[c]
        cur['$'] += 1
    for query in queries:
        if query[0] == 1:
            p = query[1]
            cur = trie
            for c in p:
                if c not in cur:
                    print(0)
                    break
                cur = cur[c]
            else:
                print(cur['$'])
        else:
            s = query[1]
            i = bisect_left(words, words[s - 1])
            cnt = 0
            while i < n and words[i].find(words[s - 1]) != -1:
                cnt += 1
                i += 1
            print(cnt)

n = int(input())
words = [input() for _ in range(n)]
q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]
solve(words, queries)

