
A, B = map(int, input().split())

for price in range(1, 1000000):
    if (price * 8 // 100 == A and price * 10 // 100 == B) or (price * 8 // 100 == B and price * 10 // 100 == A):
        print(price)
        break
else:
    print(-1)

