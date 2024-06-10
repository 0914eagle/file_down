
M = int(input())
M_set = set(map(int, input().split()))
N = int(input())
N_set = set(map(int, input().split()))

symmetric_difference = M_set.symmetric_difference(N_set)
for i in sorted(symmetric_difference):
    print(i)

