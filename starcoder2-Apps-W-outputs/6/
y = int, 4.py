
y = int(input())

while True:
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        break
    y += 1

print(y)
