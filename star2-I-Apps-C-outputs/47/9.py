
from bisect import bisect_left

def solve(words, queries):
    res = []
    for t, p in queries:
        if t == 1:
            words.append(p)
        else:
            cnt = 0
            for w in words:
                pos = bisect_left(w, p)
                if pos < len(w) and w[pos:].startswith(p):
                    cnt += 1
            res.append(cnt)
    return res

