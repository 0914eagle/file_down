
def monster_battle(A,B,C,D):
    while True:
        if A <= 0 or C <= 0:
            if A <= 0:
                return "Yes"
            else:
                return "No"
        else:
            if A > C:
                C -= D
                A -= B
            else:
                A -= D
                C -= B

print(monster_battle(int(input()),int(input()),int(input()),int(input())))

