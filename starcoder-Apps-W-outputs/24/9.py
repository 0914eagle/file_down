
import itertools

def gen_com(a):
    for i in range(1, len(a) + 1):
        for j in itertools.combinations(a, i):
            yield j

def get_ans(l):
    a = [0]
    for i in l:
        for j in gen_com(a):
            if sum(j) == i:
                return False
        a.append(i)
    return True


n = int(input())
l = []
for i in range(2 ** n):
    l.append(int(input()))
l.sort()
if get_ans(l):
    print(0)
    for i in range(1, 2 ** n):
        print(l[i] - l[i - 1])
else:
    print('impossible')

