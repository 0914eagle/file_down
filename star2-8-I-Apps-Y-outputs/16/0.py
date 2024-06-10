
N = int(input())
A = list(map(int, input().split()))

total_cost = 0
cost_to_0 = [0] * N
for i in range(N):
    total_cost += abs(A[i])
    cost_to_0[i] = total_cost

total_cost = 0
cost_from_0 = [0] * N
for i in range(N - 1, -1, -1):
    total_cost += abs(A[i])
    cost_from_0[i] = total_cost

for i in range(N):
    cost = cost_to_0[i - 1] + cost_from_0[i + 1]
    print(cost)

