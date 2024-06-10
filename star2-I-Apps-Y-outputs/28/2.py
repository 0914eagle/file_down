
N, M = map(int, input().split())
S, C = [0] * N, [0] * N
for i in range(M):
    s, c = map(int, input().split())
    S[s-1] = 1
    C[s-1] = c

def check(num):
    num_str = str(num)
    if len(num_str) != N:
        return False
    for i in range(N):
        if S[i] == 1 and int(num_str[i]) != C[i]:
            return False
    return True

ans = -1
for i in range(10 ** (N-1), 10 ** N):
    if check(i):
        ans = i
        break
print(ans)

