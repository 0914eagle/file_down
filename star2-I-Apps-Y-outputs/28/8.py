
N, M = map(int, input().split())
S, C = [0] * N, [0] * N
for i in range(M):
    s, c = map(int, input().split())
    S[s - 1] = c
for i in range(N):
    if S[i] != 0:
        continue
    for j in range(10):
        if i == 0 and j == 0:
            continue
        if i > 0 and j == S[i - 1]:
            continue
        S[i] = j
        break
    else:
        print(-1)
        exit()
print(int(''.join(map(str, S))))

