
import collections
n = int(raw_input())
l = raw_input().split()
d = collections.OrderedDict()
for i in range(len(l)):
    d[l[i]] = []
for i in range(n):
    s = raw_input().split()
    for j in range(len(l)):
        d[l[j]].append(s[j])
for i in range(len(d['MARKS'])):
    print "%.2f" % (sum(map(float,d['MARKS']))/len(d['MARKS']))

