
def toad_ivan(n, m, pairs):
    pass
n, m = [int(i) for i in input().split()]
pairs = []
for _ in range(m):
    pairs.append(tuple([int(i) for i in input().split()]))
print(toad_ivan(n, m, pairs))

