
def find_min_operation(s):
  n = len(s)
  if n == 0:
    return 0
  if n == 1:
    return 0
  if s[0] == s[1]:
    return 1
  return 0

t = int(input())
for i in range(t):
  s = input()
  print(find_min_operation(s))

