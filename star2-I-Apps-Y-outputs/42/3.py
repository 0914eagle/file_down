
M = int(input())
Mset = set(map(int, input().split()))
N = int(input())
Nset = set(map(int, input().split()))

result = sorted(Mset.symmetric_difference(Nset))
for i in result:
    print(i)

