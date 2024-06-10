
from sys import stdin
def main():
  n, p, k = map(int, stdin.readline().split())
  t = list(map(int, stdin.readline().split()))
  if n == 1:
    print((k - t[0]) / (1 + p / 100) + t[0])
  else:
    s, e = 0, k
    for i in range(n):
      s += (t[i] - s) / (1 + p * i / 100)
    print(s)
if __name__ == "__main__":
  main()

