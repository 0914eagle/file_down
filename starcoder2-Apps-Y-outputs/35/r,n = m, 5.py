
r,n = map(int,input().split())
booked = []
for i in range(n):
    booked.append(int(input()))

for i in range(1,r+1):
    if i not in booked:
        print(i)
        break
else:
    print("too late")

