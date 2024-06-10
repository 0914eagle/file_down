
N, M = map(int, input().split())
S, C = [], []
for _ in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)

def check(num):
    num_str = str(num)
    for s, c in zip(S, C):
        if num_str[s-1] != str(c):
            return False
    return True

ans = -1
for i in range(10 ** (N-1), 10 ** N):
    if check(i):
        ans = i
        break
print(ans)

