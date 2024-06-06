
import itertools
n = int(input())
a = list(map(int,input().split()))
mx = -1
for i in range(n):
    mx = max(mx,sum(list(itertools.islice(itertools.cycle(a),i,i+3))))
print(mx)
