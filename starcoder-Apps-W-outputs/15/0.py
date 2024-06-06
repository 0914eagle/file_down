

# cook your dish here
from bisect import bisect_left as bl
from bisect import bisect_right as br
import sys
sys.setrecursionlimit(10**6)
n = int(input())
a = []

def solve():
    a.sort()
    n = int(input())
    for i in range(n):
        t,x,y = map(int,input().split())
        if t==1:
            a.append((x,y))
        else:
            if x==y:
                print("NO")
            else:
                if (x,y) in a:
                    print("YES")
                else:
                    if x>y:
                        x,y = y,x
                    x1,y1 = a[bl(a,(x,))]
                    x2,y2 = a[br(a,(y,))-1]
                    if x1<x<y<y1 and x2<x<y<y2:
                        print("YES")
                    else:
                        print("NO")

solve()
