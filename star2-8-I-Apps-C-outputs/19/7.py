
from queue import Queue

def bfs(start, end, words):
  queue = Queue()
  queue.put(start)
  visited = set()
  visited.add(start)
  parent = dict()
  parent[start] = None
  while not queue.empty():
    current_word = queue.get()
    if current_word == end:
      break
    for i in range(len(current_word)):
      for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        new_word = current_word[:i] + char + current_word[i+1:]
        if new_word in words and new_word not in visited:
          queue.put(new_word)
          visited.add(new_word)
          parent[new_word] = current_word
  if end not in visited:
    return 0
  path = [end]
  current_word = end
  while parent[current_word] is not None:
    path.append(parent[current_word])
    current_word = parent[current_word]
  return len(path)-1

n = int(input())
words = set()
for i in range(n):
  words.add(input())
start = input()
end = input()
min_steps = bfs(start, end, words)
if min_steps == 0:
  print(0)
  print(-1)
else:
  for word in words:
    if bfs(start, end, words.union({word})) < min_steps:
      print(word)
      print(min_steps)
      break

