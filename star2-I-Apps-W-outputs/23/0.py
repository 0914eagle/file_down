
x = input()
x = str(x)
x = x.lstrip("0")
if x == x[::-1]:
    print("YES")
else:
    print("NO")

