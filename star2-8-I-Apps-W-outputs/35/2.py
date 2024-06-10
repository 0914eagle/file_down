
import sys
sys.stdin = open('input.txt', 'r')

def is_white(a, x, y):
  return a[x][y] == '.'

def check(a, x, y):
  if is_white(a, x, y) and is_white(a, x+1, y) and is_white(a, x, y+1) and is_white(a, x+1, y+1):
    return True
  if not is_white(a, x, y) and not is_white(a, x+1, y) and not is_white(a, x, y+1) and not is_white(a, x+1, y+1):
    return True
  return False

a = []
for i in range(4):
  a.append(input())

flag = False
for i in range(3):
  for j in range(3):
    if check(a, i, j):
      flag = True
      break
  if flag:
    break

if flag:
  print('YES')
else:
  print('NO')

