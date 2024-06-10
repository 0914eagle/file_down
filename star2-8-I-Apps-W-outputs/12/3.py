

def football_drive(drive):
  current_yard_line = 20
  for yards in drive:
    current_yard_line += yards
    if current_yard_line >= 80:
      return "Touchdown"
    elif current_yard_line <= 0:
      return "Safety"

  return "Nothing"

n = int(input())
drive = list(map(int, input().split()))
print(football_drive(drive))


