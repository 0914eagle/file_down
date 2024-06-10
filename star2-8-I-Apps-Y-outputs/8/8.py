
from sys import stdin
def playfair(key, text):
  key = key.replace(" ", "")
  table = [["" for j in range(5)] for i in range(5)]
  i = 0
  for row in table:
    for j in range(5):
      if i < len(key):
        while key[i] in [c for r in table for c in r]:
          i += 1
        row[j] = key[i]
        i += 1
      else:
        while chr(ord('a') + i) in [c for r in table for c in r]:
          i += 1
        row[j] = chr(ord('a') + i)
        i += 1
  def encrypt(a, b):
    if a == b:
      return encrypt(a, 'x')
    x1, y1 = -1, -1
    x2, y2 = -1, -1
    for i, row in enumerate(table):
      for j, c in enumerate(row):
        if c == a:
          x1, y1 = i, j
        if c == b:
          x2, y2 = i, j
    if x1 == x2:
      return table[x1][(y1 + 1) % 5] + table[x2][(y2 + 1) % 5]
    elif y1 == y2:
      return table[(x1 + 1) % 5][y1] + table[(x2 + 1) % 5][y2]
    else:
      return table[x1][y2] + table[x2][y1]
  text = text.replace(" ", "")
  text = ''.join([a + b for a, b in zip(text, text[1:] + "x") if a != b])
  return ''.join([encrypt(a, b) for a, b in zip(text, text[1:])]).upper()
key, text = [line.strip() for line in stdin.readlines()]
print(playfair(key, text))

