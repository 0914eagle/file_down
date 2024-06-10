
import sys

def main():
  n = int(sys.stdin.readline())
  yards = list(map(int, sys.stdin.readline().split()))
  total = 0
  for yard in yards:
    total += yard
    if total >= 80:
      print("Touchdown")
      return
  if total <= -20:
    print("Safety")
  else:
    print("Nothing")

if __name__ == "__main__":
  main()

