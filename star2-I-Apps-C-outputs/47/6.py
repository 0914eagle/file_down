
from bisect import bisect_left

class SuffixArray:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.sa = self._build_sa()
        self.lcp = self._build_lcp()
    
    def _build_sa(self):
        sa = []
        for i in range(self.n):
            sa.append(i)
        sa.sort(key=lambda i: self.s[i:])
        return sa
    
    def _build_lcp(self):
        lcp = [0] * self.n
        rank = [0] * self.n
        for i in range(self.n):
            rank[self.sa[i]] = i
        for i in range(self.n):
            j = self.sa[rank[i] - 1]
            k = max(j + lcp[rank[i] - 1] - 1, i)
            while k < self.n and self.s[i + k - i] == self.s[j + k - j]:
                k += 1
            lcp[rank[i] - 1] = k - i
        return lcp
    
    def find_substring(self, p):
        i = bisect_left(self.sa, 0, self.n, lambda i: self.s[i:].startswith(p))
        j = bisect_left(self.sa, i, self.n, lambda i: not self.s[i:].startswith(p))
        return i, j
    
    def count_substring(self, p):
        i, j = self.find_substring(p)
        return j - i

def solve(words, queries):
    sa = SuffixArray("".join(words))
    for t, p in queries:
        if t == 1:
            sa = SuffixArray(p + "$" + "".join(words))
            words = [p]
        else:
            print(sa.count_substring(p))

n = int(input())
words = [input() for _ in range(n)]
q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]
solve(words, queries)

