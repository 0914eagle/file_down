
A, B = map(int, input().split())

for price in range(1, 10000):
    if (price * 8 // 100 == A) and (price * 10 // 100 == B):
        print(price)
        break
else:
    print(-1)

