
import numpy as np
from collections import Counter
n,m = map(int,input().split())
a = list(map(int,input().split()))
d = dict(Counter(a))
s = np.array(list(d.values()))
if s.size == 0:
    print(0)
else:
    print(np.min(s)//n)
