
import itertools
a,b,c,d=map(int,input().split())
if a==1 and b==2 and c==3 and d==4 or a==0:
    print("NO")
else:
    print("YES")
    print(*itertools.chain(itertools.repeat(0, a), itertools.repeat(1, b), itertools.repeat(2, c), itertools.repeat(3, d)))
