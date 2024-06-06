
a, b, l, r = [int(i) for i in input().split()]
l = l - (l - 1) % a
r = r - (r - 1) % a
print((r - l) // a + 1)
