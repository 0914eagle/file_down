
def monster_battle(A,B,C,D):
    while A >= 0 and C >= 0:
        if A > C:
            C -= B
        elif A < C:
            A -= D
        else:
            A -= B
            C -= D
    return "Yes" if A < 0 else "No"

