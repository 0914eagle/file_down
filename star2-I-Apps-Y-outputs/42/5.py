
m = int(input())
m_set = set(map(int, input().split()))
n = int(input())
n_set = set(map(int, input().split()))

symmetric_difference = m_set.symmetric_difference(n_set)
for i in sorted(symmetric_difference):
    print(i)

