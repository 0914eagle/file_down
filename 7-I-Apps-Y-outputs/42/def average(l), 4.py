
import collections

def average(l):
    return sum(l) / len(l)

n = int(input())
l = []
for i in range(n):
    l.append(list(map(float, input().split())))

l = collections.namedtuple('l', input().split())(*l)
print("{:.2f}".format(average(l.MARKS)))

