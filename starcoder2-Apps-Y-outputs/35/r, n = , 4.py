
r, n = map(int, input().split())
booked = set()
for i in range(n):
    booked.add(int(input()))

for i in range(1, r+1):
    if i not in booked:
        print(i)
        break
else:
    print("too late")

