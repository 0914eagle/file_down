
S = input()

T = [input().split() for _ in range(26)]

K = int(input())

M = int(input())

m = [int(x) for x in input().split()]

def f(c):
  return T[ord(c) - ord('a')]

def fK(S):
  for _ in range(K):
    newS = ""
    for c in S:
      newS += f(c)
    
    S = newS
  return S

P = fK(S)

for i in m:
  print(P[i - 1])

