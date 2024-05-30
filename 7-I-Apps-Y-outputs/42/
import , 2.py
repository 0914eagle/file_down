
import collections
n = int(input())
l = input().split()
d = collections.OrderedDict()
for i in range(n):
    l = input().split()
    for j in range(len(l)):
        if l[j] not in d:
            d[l[j]] = [l[j+1]]
        else:
            d[l[j]].append(l[j+1])
for i in d:
    if i == 'MARKS':
        print('{:.2f}'.format(sum(map(float,d[i]))/len(d[i])))

