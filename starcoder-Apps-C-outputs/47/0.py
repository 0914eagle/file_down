
a = int(input())
b = int(input())
if a >= b and b <= 26:
    print(b*'a' + (a-b)*'b')
else:
    print(-1)
