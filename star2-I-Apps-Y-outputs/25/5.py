
A, B = map(int, input().split())
for i in range(1, 100000):
    if (i * 8 // 100 == A and i * 10 // 100 == B) or (i * 8 // 100 == B and i * 10 // 100 == A):
        print(i)
        break
else:
    print(-1)

