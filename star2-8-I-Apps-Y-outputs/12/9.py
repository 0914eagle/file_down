
def print_time(h, m):
print(h, m)
h, m = map(int, input().split())
if m >= 45:
m -= 45
else:
h -= 1
if h < 0:
h += 24
m += 15
print_time(h, m)

