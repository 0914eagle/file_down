
import sys

input = sys.stdin.readline

def f(s):
    ret = ""
    for c in s:
        ret += T[ord(c) - ord('a')]
    return ret

S = input().rstrip()
T = [input().rstrip() for _ in range(26)]
K = int(input())
M = int(input())
pos = [int(input()) for _ in range(M)]

def get_length(n):
    if n <= len(S):
        return len(S)
    ret = 0
    while n > 0:
        ret += len(f(S))
        n -= 1
    return ret

def get_char(n):
    if n <= len(S):
        return S[n-1]
    n -= len(S)
    while n > 0:
        S = f(S)
        n -= len(S)
    return S[n-1]

left = 1
right = 10**15
while left < right:
    mid = (left + right) // 2
    if get_length(mid) >= pos[0]:
        right = mid
    else:
        left = mid + 1

for p in pos:
    print(get_char(p))

