
n = int(input())
usb = 0
ps2 = 0
usb_cost = 0
ps2_cost = 0
for i in range(n):
    cost, port = input().split()
    cost = int(cost)
    if port == "USB":
        usb += 1
        usb_cost += cost
    else:
        ps2 += 1
        ps2_cost += cost

a, b, c = map(int, input().split())

total = min(a, usb) + min(b, ps2) + min(c, usb + ps2)
cost = min(a, usb) * usb_cost + min(b, ps2) * ps2_cost + min(c, usb + ps2) * min(usb_cost, ps2_cost)
print(total, cost)

