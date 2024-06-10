
from bisect import bisect_left

def find_substrings(words, q):
    for t, p in q:
        if t == 1:
            words.append(p)
        else:
            count = 0
            for word in words:
                i = bisect_left(word, p)
                if i != len(word) and word.startswith(p, i):
                    count += 1
            print(count)

n = int(input())
words = [input() for _ in range(n)]
q = int(input())
q = [(int(x), y) for x, y in (input().split() for _ in range(q))]
find_substrings(words, q)

