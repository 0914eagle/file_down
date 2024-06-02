
r, n = map(int, input().split())
booked = set(map(int, [input() for _ in range(n)]))
for i in range(1, r + 1):
    if i not in booked:
        print(i)
        break
else:
    print('too late')

