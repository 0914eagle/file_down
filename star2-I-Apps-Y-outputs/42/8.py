
M = int(input())
M_list = map(int, input().split())
N = int(input())
N_list = map(int, input().split())

M_set = set(M_list)
N_set = set(N_list)

result = M_set.symmetric_difference(N_set)

for i in sorted(result):
    print(i)

