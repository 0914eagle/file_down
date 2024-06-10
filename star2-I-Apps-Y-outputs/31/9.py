
g, s, c = map(int, input().split())
buying_power = 2 * s + 1 * c
if buying_power >= 8:
    print("Province")
elif buying_power >= 5:
    print("Duchy")
elif buying_power >= 2:
    print("Estate")
if buying_power >= 6:
    print("Gold")
elif buying_power >= 3:
    print("Silver")
elif buying_power >= 1:
    print("Copper")

