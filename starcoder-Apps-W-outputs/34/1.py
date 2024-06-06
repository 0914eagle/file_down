
from sys import stdin
N = int(stdin.readline())
data = []
data_re = []
for i in range(N):
    name,ty = stdin.readline().split()
    ty = int(ty)
    if ty:
        data.append((name,ty))
    else:
        data_re.append((name,ty))

res = []
for i,d in enumerate(data):
    res.append(("move %s %d"%(d[0],i+1)))
for i,d in enumerate(data_re):
    res.append(("move %s %d"%(d[0],len(data)+i+1)))
print(len(res))
print('\n'.join(res))
