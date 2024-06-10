
n, m, p = list(map(int, input().split()))
s = input()
q = input()

def find_pair(s, p):
  if s[p-1] == "(":
    for j in range(p, len(s)):
      if s[j] == ")":
        return j+1
  else:
    for j in range(p-2, -1, -1):
      if s[j] == "(":
        return j+1

def del_pair(s, p):
  p = find_pair(s, p)
  return s[:p-1] + s[p:]

for c in q:
  if c == "L" and p > 1:
    p -= 1
  elif c == "R" and p < len(s):
    p += 1
  elif c == "D":
    s = del_pair(s, p)
    p = find_pair(s, p)
    
print(s)

