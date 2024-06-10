
from sys import stdin
s = next(stdin)
t = [next(stdin).split() for _ in range(26)]
k = int(next(stdin))
m = int(next(stdin))
m = [int(i) for i in next(stdin).split()]
def f(ch):
    return t[ord(ch)-ord('a')]
def get(index, k):
    if index < len(s):
        return s[index]
    index -= len(s)
    for i in range(k):
        index -= 1
        for j in range(len(t)):
            if index < len(t[j]):
                return t[j][index]
            index -= len(t[j])
for i in m:
    print(get(i, k))

