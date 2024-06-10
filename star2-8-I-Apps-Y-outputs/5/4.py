
n, c = [int(x) for x in input().split()]
fruits = [int(x) for x in input().split()]

fruits.sort()

capacity = c
total_fruits = 0

for fruit in fruits:
  if fruit <= capacity:
    capacity -= fruit
    total_fruits += 1
  else:
    break

print(total_fruits)

