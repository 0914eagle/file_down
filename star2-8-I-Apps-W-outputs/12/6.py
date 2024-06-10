
def main():
  n = int(input())
  yards = [int(x) for x in input().split()]

  touchdown = False
  safety = False
  first_down = 0

  for yard in yards:
    if first_down >= 10:
      touchdown = True
      break
    
    if yard >= 10:
      first_down += yard
    
    elif yard <= -20:
      safety = True
      break
  if touchdown:
    print("Touchdown")
  elif safety:
    print("Safety")
  else:
    print("Nothing")

if __name__ == '__main__':
  main()

