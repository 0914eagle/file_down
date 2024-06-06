
#!/usr/bin/python

import math,string,itertools,fractions,heapq,collections,re,array,bisect,random

def main():
    n, d, c = map(int, raw_input().strip().split())
    cards = [set(map(int, raw_input().strip().split())) for i in xrange(2)]
    comb = itertools.combinations(range(1, n + 1), c)
    comb = list(comb)
    sum = 0.0
    for i in comb:
        for j in comb:
            if i != j:
                sum += play(set(i), set(j), d, n)
    print (sum / ((n - c) * (n - c)))

def play(a, b, d, n):
    cnt = 0
    while a and b:
        x = set(random.sample(range(1, n + 1), d))
        a -= x
        b -= x
        cnt += 1
    return cnt

main()
