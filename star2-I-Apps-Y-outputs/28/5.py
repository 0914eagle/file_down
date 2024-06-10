
N, M = map(int, input().split())
S, C = [], []
for i in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)

def check(num):
    num_str = str(num)
    for i in range(M):
        if num_str[S[i]-1] != str(C[i]):
            return False
    return True

ans = -1
for i in range(10**(N-1), 10**N):
    if check(i):
        ans = i
        break
print(ans)

