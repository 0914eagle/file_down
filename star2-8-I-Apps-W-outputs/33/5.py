
from itertools import product

def parse_commands(s):
  pos = 0
  for c in s:
    if c == '+':
      pos += 1
    elif c == '-':
      pos -= 1
  return pos

def check_command(c, d):
  if c == '?':
    return d == '+' or d == '-'
  else:
    return c == d

s1 = input()
s2 = input()

if len(s1) != len(s2):
  raise Exception("Invalid input")

total_pos = 0
correct_pos = 0

for comb in product([ '+', '-' ], repeat=s2.count('?')):
  pos = 0
  for i in range(len(s2)):
    if check_command(s2[i], comb[i] if s2[i] == '?' else s2[i]):
      if comb[i] == '+':
        pos += 1
      elif comb[i] == '-':
        pos -= 1

  if pos == parse_commands(s1):
    correct_pos += 1
  total_pos += 1

print(correct_pos / total_pos)

