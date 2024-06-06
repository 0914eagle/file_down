
#import sys
#input = sys.stdin.readline
import bisect
n,m = map(int,input().split())
a = list(map(int,input().split()))
d = []
for i in range(m):
    d.append(list(map(int,input().split())))
d.sort()
for i in range(m):
    bisect.insort(a,d[i][0])
    x = bisect.bisect_right(a,d[i][0])
    print(x*d[i][1],end = ' ')
