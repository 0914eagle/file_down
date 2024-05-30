
import collections

def average(lst):
    return sum(lst) / len(lst)

def marks(n, m, c, nm):
    return average(m)

if __name__ == '__main__':
    n = int(input())
    l = list(map(str, input().split()))
    d = {}
    for i in l:
        d[i] = []
    for i in range(n):
        s = list(map(str, input().split()))
        for j in range(len(s)):
            d[l[j]].append(s[j])
    for i in d:
        print(i, d[i])
    print(marks(n, d['MARKS'], d['CLASS'], d['NAME']))

