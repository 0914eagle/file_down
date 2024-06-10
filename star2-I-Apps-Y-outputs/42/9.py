
m = int(input())
mset = set(map(int, input().split()))
n = int(input())
nset = set(map(int, input().split()))

for i in sorted(mset.symmetric_difference(nset)):
    print(i)

