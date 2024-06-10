
A, B, C = map(int, input().split())
if C % B == 0:
  print("YES")
elif C % B == A % B:
  print("YES")
else:
  print("NO")

