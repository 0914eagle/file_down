
import sys
def read_input():
  line = input()
  n = int(line)
  dictionary = []
  for i in range(n):
    line = input()
    dictionary.append(line)
  return dictionary
def find_ladder(dictionary, start_word, end_word):
  visited = set()
  queue = []
  queue.append((start_word, 0))
  visited.add(start_word)
  while len(queue) > 0:
    word, steps = queue.pop(0)
    for i in range(len(word)):
      for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        new_word = word[:i] + c + word[i+1:]
        if new_word == end_word:
          return (new_word, steps + 1)
        if new_word in dictionary and new_word not in visited:
          queue.append((new_word, steps + 1))
          visited.add(new_word)
  return (None, None)
def main():
  dictionary = read_input()
  start_word = dictionary[0]
  end_word = dictionary[1]
  new_word, steps = find_ladder(dictionary, start_word, end_word)
  if new_word is None:
    print('0')
    print('-1')
  else:
    print(new_word)
    print(steps)
main()

