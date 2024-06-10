
g, s, c = map(int, input().split())
vp = 6 * (g >= 8) + 3 * (s >= 5) + (c >= 2)
tp = 3 * (g >= 6) + 2 * (s >= 3) + (c >= 0)
if tp >= vp:
    print("Gold" if g >= 6 else "Silver" if s >= 3 else "Copper")
else:
    print("Province" if g >= 8 else "Duchy" if s >= 5 else "Estate" if c >= 2 else "Copper")

