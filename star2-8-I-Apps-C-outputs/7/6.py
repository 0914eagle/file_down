
def f(s):
    res = ""
    for c in s:
        res += T[c]
    return res
S = input()
T = {}
for c in "abcdefghijklm":
    T[c] = input()
for c in "nopqrstuvwxyz":
    T[c] = input()
K = int(input())
M = int(input())
pos = [int(i) for i in input().split()]
for i in range(K):
    S = f(S)
for i in pos:
    print(S[i-1])

