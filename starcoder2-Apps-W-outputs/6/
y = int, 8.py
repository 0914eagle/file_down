
y = int(input())

while True:
    y += 1
    if y % 400 == 0:
        break
    elif y % 100 == 0:
        continue
    elif y % 4 == 0:
        break
print(y)
