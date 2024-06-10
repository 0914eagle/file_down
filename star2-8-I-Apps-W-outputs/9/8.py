
H, N = map(int, input().split())
spells = []
for i in range(N):
    spells.append(tuple(map(int, input().split())))

def cast_spell(spells, health):
    min_cost = None
    min_spell = None
    for spell in spells:
        cost = spell[1]
        if health - spell[0] <= 0:
            return cost
        else:
            if min_cost is None or cost < min_cost:
                min_cost = cost
                min_spell = spell
    health -= min_spell[0]
    return cost + cast_spell(spells, health)

print(cast_spell(spells, H))

