
def main():
  n, m, k = map(int, input().split())
  buildings = [0] * (m + 1)
  for i in range(n):
    buildings[int(input())] += 1
  buildings.sort()
  best = sum(buildings)
  for i in range(k):
    best -= buildings[-1]
    buildings[-1] = 0
  print(best)
if __name__ == '__main__':
  main()

