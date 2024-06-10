
from itertools import permutations

def prob_all_dead(my_minions, opp_minions, dmg):
    my_minions = sorted(my_minions, reverse=True)
    opp_minions = sorted(opp_minions, reverse=True)
    my_perm = permutations(my_minions)
    opp_perm = permutations(opp_minions)
    prob = 0
    for my_perm_i in my_perm:
        for opp_perm_i in opp_perm:
            my_perm_i = list(my_perm_i)
            opp_perm_i = list(opp_perm_i)
            my_perm_i = [x - 1 for x in my_perm_i]
            opp_perm_i = [x - 1 for x in opp_perm_i]
            if sum(my_perm_i) >= dmg and sum(opp_perm_i) >= dmg:
                prob += 1
    prob /= len(my_minions) ** len(my_minions) * len(opp_minions) ** len(opp_minions)
    return prob

n, m, d = map(int, input().split())
my_minions = list(map(int, input().split()))
opp_minions = list(map(int, input().split()))
print(prob_all_dead(my_minions, opp_minions, d))

