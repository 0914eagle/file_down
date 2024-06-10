
N, M = map(int, input().split())
S = [0] * N
for _ in range(M):
    s, c = map(int, input().split())
    S[s - 1] = c
for i in range(10 ** (N - 1), 10 ** N):
    i_str = str(i)
    if all(i_str[s - 1] == str(c) for s, c in zip(S, S) if s != 0):
        print(i)
        break
else:
    print(-1)

