
S, C, K = map(int, input().split())
D = list(map(int, input().split()))
D = sorted(D)
n_machine = 1
num_sock = 1
for i in range(1, S):
    if D[i] - D[i-1] <= K and num_sock < C:
        num_sock += 1
    else:
        n_machine += 1
        num_sock = 1
print(n_machine)

