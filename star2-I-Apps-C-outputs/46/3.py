
import sys

def solve(boys, girls):
  boys_books = {}
  girls_books = {}
  for boy in boys:
    boys_books[boy] = set()
  for girl in girls:
    girls_books[girl] = set()
  for boy in boys:
    for book in boys[boy]:
      boys_books[boy].add(book)
      girls_books[boy].add(book)
  for girl in girls:
    for book in girls[girl]:
      boys_books[girl].add(book)
      girls_books[girl].add(book)
  presentations = 0
  for boy in boys_books:
    if len(boys_books[boy]) > 0:
      presentations += 1
  for girl in girls_books:
    if len(girls_books[girl]) > 0:
      presentations += 1
  return presentations

def main():
  boys = {}
  girls = {}
  first_line = sys.stdin.readline().strip().split()
  B = int(first_line[0])
  G = int(first_line[1])
  for i in range(B):
    line = sys.stdin.readline().strip().split()
    name = line[0]
    N = int(line[1])
    books = line[2:]
    boys[name] = books
  for i in range(G):
    line = sys.stdin.readline().strip().split()
    name = line[0]
    N = int(line[1])
    books = line[2:]
    girls[name] = books
  print(solve(boys, girls))

if __name__ == "__main__":
  main()

