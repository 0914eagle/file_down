
import sys
from itertools import combinations
def process(combs):
    hs = []
    ws = []
    for i in combs:
        w = 0
        h = []
        for j in i:
            w += books[j][1]
            h.append(books[j][0])
        hs.append(max(h))
        ws.append(w)
    return max(hs)*sum(ws)

books = []
for line in sys.stdin:
    books.append(tuple(int(i) for i in line.split()))

comb = []
for i in range(1,len(books)//2+1):
    comb.extend(combinations(range(len(books)),i))

min_area = float('inf')
for combi in comb:
    rest = set(range(len(books))) - set(combi)
    rest_combs = combinations(rest,len(rest)//2)
    for rest_comb in rest_combs:
        area = process(combi) + process(rest_comb)
        min_area = min(area,min_area)
print(min_area)
