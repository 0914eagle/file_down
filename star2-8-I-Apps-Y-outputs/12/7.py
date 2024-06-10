
h, m = map(int, input().split())
h -= (m - 45) // 60
m = (m - 45) % 60
if m < 0:
    h -= 1
    m += 60
if h < 0:
    h += 24
print(h, m)

