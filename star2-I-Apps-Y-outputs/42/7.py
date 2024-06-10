
M = int(input())
set_M = set(map(int, input().split()))
N = int(input())
set_N = set(map(int, input().split()))

symmetric_difference = set_M.symmetric_difference(set_N)
for i in sorted(symmetric_difference):
    print(i)

