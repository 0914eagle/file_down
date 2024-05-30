
def monster_battle(A,B,C,D):
    while A >= 0 and C >= 0:
        if A > C:
            C -= B
            if C < 0:
                return "Yes"
        else:
            A -= D
            if A < 0:
                return "No"
    return "Yes"

