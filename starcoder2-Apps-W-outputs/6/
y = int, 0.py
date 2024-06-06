
y = int(input())

while True:
    y += 1
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        break

print(y)
