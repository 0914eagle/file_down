
import sys

def word_ladder():
  n = int(input())
  dictionary = set()
  for i in range(n):
    dictionary.add(input())
  start_word = input()
  end_word = input()
  length = len(start_word)
  queue = [(start_word, 0)]
  visited = set()
  while queue:
    word, distance = queue.pop(0)
    if word == end_word:
      return distance
    for i in range(length):
      for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        new_word = word[:i] + ch + word[i+1:]
        if new_word in dictionary and new_word not in visited:
          queue.append((new_word, distance+1))
          visited.add(new_word)
  return 0

if __name__ == '__main__':
  n = int(input())
  dictionary = set()
  for i in range(n):
    dictionary.add(input())
  start_word = input()
  end_word = input()
  length = len(start_word)
  queue = [(start_word, 0)]
  visited = set()
  while queue:
    word, distance = queue.pop(0)
    if word == end_word:
      print(word)
      print(distance)
      sys.exit()
    for i in range(length):
      for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        new_word = word[:i] + ch + word[i+1:]
        if new_word in dictionary and new_word not in visited:
          queue.append((new_word, distance+1))
          visited.add(new_word)
  print(0)
  print(-1)

