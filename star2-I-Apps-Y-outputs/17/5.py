
s = input()
t = input()

if s == t:
  print("Yes")
elif s == t[::-1]:
  print("Yes")
else:
  print("No")

