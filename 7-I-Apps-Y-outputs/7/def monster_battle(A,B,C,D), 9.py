
def monster_battle(A,B,C,D):
    while True:
        if A <= 0:
            return "No"
        if C <= 0:
            return "Yes"
        A -= max(B,D)
        C -= min(B,D)

print(monster_battle(int(input()),int(input()),int(input()),int(input())))

