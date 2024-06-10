
import re
def check(s):
  if re.search(r"010|101",s):
    return False
  return True
def solve(s):
  if check(s):
    return 0
  if s[0] == "0":
    return 1+solve(s[1:].replace("1","0",1))
  return 1+solve(s[1:].replace("0","1",1))

t = int(input())
for _ in range(t):
  s = input()
  print(solve(s))

