
def max_damage(pillars):
    max_damage = 1
    max_damage_pillar = 0
    for i, pillar in enumerate(pillars):
        damage = 1
        weight = pillar
        for j in range(i - 1, -1, -1):
            weight += pillars[j]
            if weight > pillars[j]:
                damage += 1
            else:
                break
        for j in range(i + 1, len(pillars)):
            weight += pillars[j]
            if weight > pillars[j]:
                damage += 1
            else:
                break
        if damage > max_damage:
            max_damage = damage
            max_damage_pillar = i
    return max_damage, max_damage_pillar


n = int(input())
pillars = list(map(int, input().split()))
max_damage, max_damage_pillar = max_damage(pillars)
print(max_damage, max_damage_pillar)

