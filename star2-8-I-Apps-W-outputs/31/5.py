
a, b, c = map(int, input().split())
m = int(input())
usb = []
ps2 = []
for _ in range(m):
    val, port = input().split()
    val = int(val)
    if port == 'USB':
        usb.append(val)
    else:
        ps2.append(val)

usb.sort()
ps2.sort()

ans = 0
cost = 0

i = 0
j = 0

while i < len(usb) and j < len(ps2):
    if usb[i] + ps2[j] <= 10:
        cost += usb[i] + ps2[j]
        i += 1
        j += 1
        ans += 1
    else:
        break

while i < len(usb) and ans + i <= a + b:
    cost += usb[i]
    i += 1
    ans += 1

while j < len(ps2) and ans + j <= a + b + c:
    cost += ps2[j]
    j += 1
    ans += 1
print(ans, cost)

