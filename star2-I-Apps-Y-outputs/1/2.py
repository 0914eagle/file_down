
n = int(input())
s = input()

x = 0
max_x = 0
for c in s:
    if c == 'I':
        x += 1
    else:
        x -= 1
    max_x = max(max_x, x)

print(max_x)

