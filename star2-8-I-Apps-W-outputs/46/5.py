
#!/usr/bin/env python3

def main():
  H = int(input())
  hotdogs = [int(s) for s in input().split()]
  B = int(input())
  buns = [int(s) for s in input().split()]

  hotdogs.sort(reverse=True)
  buns.sort(reverse=True)

  total_packs = 0
  while hotdogs and buns:
    h = hotdogs.pop()
    b = buns.pop()
    if h < b:
      hotdogs.append(h)
      h = hotdogs.pop()
    packs = max(h // b, b // h)
    total_packs += packs
    for _ in range(packs):
      hotdogs.append(h - b * packs)
      buns.append(b - h * packs)
  if hotdogs or buns:
    print("impossible")
  else:
    print(total_packs)


if __name__ == "__main__":
  main()

