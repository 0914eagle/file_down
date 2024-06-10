
import string
alphabet = string.ascii_lowercase

def f(s):
  result = ""
  for c in s:
    result += T[alphabet.index(c)]
  return result

S = input()
T = input().split() + input().split()
K = int(input())
M = int(input())
ms = list(map(int, input().split()))

S_star = S
for i in range(K):
  S_star = f(S_star)

for m in ms:
  letter_index = -1
  for i, c in enumerate(S_star):
    if c in alphabet:
      letter_index += 1
    if letter_index == m:
      print(c)
      break

