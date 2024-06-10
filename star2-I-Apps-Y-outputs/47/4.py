
n = int(input())
s = input()

def isGood(s):
  if len(s) % 2 != 0:
    return False
  for i in range(0, len(s), 2):
    if s[i] == s[i+1]:
      return False
  return True

if isGood(s):
  print(0)
  print(s)
else:
  for i in range(len(s)):
    new_s = s[:i] + s[i+1:]
    if isGood(new_s):
      print(1)
      print(new_s)
      break

