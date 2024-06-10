
N, M = map(int, input().split())
S = [0] * N
for _ in range(M):
    s, c = map(int, input().split())
    S[s-1] = c

def check(num):
    num_str = str(num)
    for i in range(N):
        if S[i] != 0 and S[i] != int(num_str[i]):
            return False
    return True

def solve():
    for i in range(10 ** (N-1), 10 ** N):
        if check(i):
            return i
    return -1

print(solve())

