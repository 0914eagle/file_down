
A, B = map(int, input().split())
price = -1
for p in range(1, 10001):
  if int(p * 0.08) == A and int(p * 0.1) == B:
    price = p
    break
print(price)

