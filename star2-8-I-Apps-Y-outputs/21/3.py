
x = int(input())
happiness = 0

for i in range(x // 500 + 1):
  for j in range(x // 5 + 1):
    if i * 500 + j * 5 > x:
      continue
    
    happiness = max(happiness, i * 1000 + j * 5)
    
print(happiness)

